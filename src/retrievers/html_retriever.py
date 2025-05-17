import hashlib
from pathlib import Path
from typing import List, Union, Optional

import psycopg2
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_postgres.vectorstores import PGVector
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from ..preprocessors.html_crawler_preprocessor import HTMLCrawlerPreprocessor
from ..utils.env_loader import load_env_vars, get_db_connection_string
from .base_retriever import BaseRetriever


class HTMLRetriever(BaseRetriever):
    """Retriever that processes web content before adding it to the vector database."""
    
    def __init__(
        self,
        connection_string: str = None,
        collection_name: str = "web_documents",
        chunk_size: int = 7000,
        chunk_overlap: int = 6800,
        embedding_model: str = "models/text-embedding-004",
        max_pages: int = 10,
        max_depth: int = 2
    ):
        """
        Initialize the HTML retriever.
        
        Args:
            connection_string: PostgreSQL connection string. If None, will use environment variables
            collection_name: Name of the collection in the database
            chunk_size: Size of text chunks for splitting
            chunk_overlap: Overlap between chunks
            embedding_model: Name of the embedding model to use
            max_pages: Maximum number of pages to crawl
            max_depth: Maximum depth of crawling
        """
        # Load environment variables
        self.env_vars = load_env_vars()
        
        # Set connection string
        self.connection_string = connection_string or get_db_connection_string()
        self.collection_name = collection_name
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Initialize preprocessor
        self.preprocessor = HTMLCrawlerPreprocessor(
            max_pages=max_pages,
            max_depth=max_depth
        )
        
        # Initialize text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            is_separator_regex=False
        )
        
        # Initialize embeddings
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model=embedding_model,
            google_api_key=self.env_vars["GOOGLE_API_KEY"]
        )
        
        # Initialize vector store
        self._init_vector_store()
    
    def _init_vector_store(self) -> None:
        """Initialize the PGVector store and create necessary tables."""
        try:
            # Create new collection with proper schema
            self.vector_store = PGVector(
                collection_name=self.collection_name,
                connection=self.connection_string,
                embeddings=self.embeddings,
                pre_delete_collection=True,
                use_jsonb=True,
            )

            print(f"✅ Successfully initialized vector store collection: {self.collection_name}")

        except Exception as e:
            print(f"❌ Fatal error initializing vector store: {str(e)}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            raise
    
    def _generate_document_id(self, url: str, chunk_index: int) -> str:
        """
        Generate a unique document ID based on URL and chunk index.
        
        Args:
            url: URL of the document
            chunk_index: Index of the chunk within the document
            
        Returns:
            str: Unique document ID
        """
        content = f"{url}_{chunk_index}".encode()
        return hashlib.md5(content).hexdigest()
    
    def _process_and_split_document(self, url: str) -> List[Document]:
        """
        Process a URL and split it into chunks.
        
        Args:
            url: URL to process
            
        Returns:
            List[Document]: List of document chunks
        """
        try:
            print(f"🔄 Processing URL: {url}")
            
            # Process URL and get markdown content
            md_path = self.preprocessor.process_url(url)
            if not md_path or not Path(md_path).exists():
                print(f"❌ Markdown file not created at {md_path}")
                return []
                
            print(f"✅ URL processed and converted to markdown: {md_path}")
            
            # Read markdown content
            try:
                with open(md_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                print(f"✅ Successfully read markdown file ({len(text)} characters)")
            except Exception as e:
                print(f"❌ Error reading markdown file: {e}")
                return []
            
            if not text.strip():
                print("❌ Markdown file is empty")
                return []
            
            # Create Document object from text
            doc = Document(page_content=text, metadata={'source': url})
            
            # Split into chunks
            print("🔄 Splitting document into chunks...")
            chunks = self.text_splitter.split_documents([doc])
            print(f"✅ Created {len(chunks)} chunks")
            
            # Add metadata to chunks
            for i, chunk in enumerate(chunks):
                chunk.metadata.update({
                    'chunk_index': i,
                    'document_id': self._generate_document_id(url, i)
                })
            
            return chunks
        except Exception as e:
            print(f"❌ Error processing URL {url}: {str(e)}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            return []
    
    def add_documents(self, urls: List[str], **kwargs) -> None:
        """
        Add web documents to the vector store.
        
        Args:
            urls: List of URLs to process and add
            **kwargs: Additional arguments (not used)
        """
        all_chunks = []
        for url in urls:
            chunks = self._process_and_split_document(url)
            all_chunks.extend(chunks)
        
        if all_chunks:
            try:
                self.vector_store.add_documents(all_chunks)
                print(f"✅ Added {len(all_chunks)} chunks from {len(urls)} URLs to vector store")
            except Exception as e:
                print(f"❌ Error adding documents to vector store: {e}")
    
    def get_relevant_documents(
        self,
        query: str,
        k: int = 4,
        filter: Optional[dict] = None,
        **kwargs
    ) -> List[Document]:
        """
        Retrieve relevant documents for a query.
        
        Args:
            query: The search query
            k: Number of documents to retrieve
            filter: Optional metadata filter
            **kwargs: Additional arguments passed to similarity search
            
        Returns:
            List[Document]: List of relevant documents
        """
        try:
            return self.vector_store.similarity_search(
                query,
                k=k,
                filter=filter,
                **kwargs
            )
        except Exception as e:
            print(f"❌ Error retrieving documents: {e}")
            return [] 