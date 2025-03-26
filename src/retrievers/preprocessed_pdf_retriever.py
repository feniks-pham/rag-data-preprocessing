import hashlib
from typing import List, Union, Optional

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres.vectorstores import PGVector
from pathlib import Path

from .base_retriever import BaseRetriever
from ..preprocessors.pdf_preprocessor import PDFPreprocessor
from ..utils.env_loader import load_env_vars, get_db_connection_string


class PreprocessedPDFRetriever(BaseRetriever):
    """Retriever that preprocesses PDFs before adding them to the vector database."""
    
    def __init__(
        self,
        connection_string: str = None,
        collection_name: str = "preprocessed_documents",
        chunk_size: int = 7000,
        chunk_overlap: int = 6800,
        embedding_model: str = "models/text-embedding-004"
    ):
        """
        Initialize the preprocessed PDF retriever.
        
        Args:
            connection_string: PostgreSQL connection string. If None, will use environment variables
            collection_name: Name of the collection in the database
            chunk_size: Size of text chunks for splitting
            chunk_overlap: Overlap between chunks
            embedding_model: Name of the embedding model to use
        """
        # Load environment variables
        self.env_vars = load_env_vars()
        
        # Set connection string
        self.connection_string = connection_string or get_db_connection_string()
        self.collection_name = collection_name
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Initialize preprocessor
        self.preprocessor = PDFPreprocessor()
        
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
    
    def _generate_document_id(self, file_path: Union[str, Path], chunk_index: int) -> str:
        """
        Generate a unique document ID based on file path and chunk index.
        
        Args:
            file_path: Path to the document
            chunk_index: Index of the chunk within the document
            
        Returns:
            str: Unique document ID
        """
        file_path = str(file_path)
        content = f"{file_path}_{chunk_index}".encode()
        return hashlib.md5(content).hexdigest()
    
    def _process_and_split_document(self, file_path: Union[str, Path]) -> List[Document]:
        """
        Process a PDF file and split it into chunks.
        
        Args:
            file_path: Path to the PDF file
            
        Returns:
            List[Document]: List of document chunks
        """
        try:
            print(f"🔄 Processing PDF file: {file_path}")
            
            # Convert PDF to markdown
            md_path = self.preprocessor.process_pdf(file_path)
            if not md_path or not Path(md_path).exists():
                print(f"❌ Markdown file not created at {md_path}")
                return []
                
            print(f"✅ PDF converted to markdown: {md_path}")
            
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
            doc = Document(page_content=text, metadata={'source': str(file_path)})
            
            # Split into chunks
            print("🔄 Splitting document into chunks...")
            chunks = self.text_splitter.split_documents([doc])
            print(f"✅ Created {len(chunks)} chunks")
            
            # Add metadata to chunks
            for i, chunk in enumerate(chunks):
                chunk.metadata.update({
                    'chunk_index': i,
                    'document_id': self._generate_document_id(file_path, i)
                })
            
            return chunks
        except Exception as e:
            print(f"❌ Error processing document {file_path}: {str(e)}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            return []
    
    def add_documents(self, file_paths: List[Union[str, Path]], **kwargs) -> None:
        """
        Add documents to the vector store.
        
        Args:
            file_paths: List of paths to PDF files
            **kwargs: Additional arguments (not used)
        """
        all_chunks = []
        for file_path in file_paths:
            chunks = self._process_and_split_document(file_path)
            all_chunks.extend(chunks)
        
        if all_chunks:
            try:
                self.vector_store.add_documents(all_chunks)
                print(f"✅ Added {len(all_chunks)} chunks from {len(file_paths)} documents to vector store")
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
    
    # def delete_documents(self, document_ids: List[str]) -> None:
    #     """
    #     Delete documents from the vector store.
    #
    #     Args:
    #         document_ids: List of document IDs to delete
    #     """
    #     try:
    #         filter = {"document_id": {"$in": document_ids}}
    #         self.vector_store.delete(filter)
    #         print(f"✅ Deleted {len(document_ids)} documents from vector store")
    #     except Exception as e:
    #         print(f"❌ Error deleting documents: {e}")