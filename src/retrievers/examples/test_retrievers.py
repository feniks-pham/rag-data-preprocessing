from pathlib import Path
from src.retrievers.preprocessed_pdf_retriever import PreprocessedPDFRetriever
from src.retrievers.direct_pdf_retriever import DirectPDFRetriever

def test_preprocessed_retriever(input_file):
    """Test the preprocessed PDF retriever."""
    # Initialize retriever
    retriever = PreprocessedPDFRetriever(
        connection_string="postgresql://admin:admin@localhost:5432/vector_db",
        collection_name="test_preprocessed",
        chunk_size=7000,
        chunk_overlap=6800
    )
    
    
    try:
        # Add document to vector store
        retriever.add_documents([input_file])
        
        # Test retrieval
        query = "What is the main topic of the document?"
        docs = retriever.get_relevant_documents(query, k=2)
        
        print("\nRetrieved documents:")
        for i, doc in enumerate(docs, 1):
            print(f"\nDocument {i}:")
            print(f"Source: {doc.metadata['source']}")
            print(f"Chunk: {doc.metadata['chunk_index']}")
            print("Content preview:", doc.page_content[:200], "...")
            
    except Exception as e:
        print(f"❌ Error testing preprocessed retriever: {e}")

def test_direct_retriever(input_file):
    """Test the direct PDF retriever."""
    # Initialize retriever
    retriever = DirectPDFRetriever(
        connection_string="postgresql://admin:admin@localhost:5432/vector_db",
        collection_name="test_direct",
        chunk_size=7000,
        chunk_overlap=6800
    )
    
    try:
        # Add document to vector store
        retriever.add_documents([input_file])
        
        # Test retrieval
        query = "What is the main topic of the document?"
        docs = retriever.get_relevant_documents(query, k=2)
        
        print("\nRetrieved documents:")
        for i, doc in enumerate(docs, 1):
            print(f"\nDocument {i}:")
            print(f"Source: {doc.metadata['source']}")
            print(f"Chunk: {doc.metadata['chunk_index']}")
            print("Content preview:", doc.page_content[:200], "...")
            
    except Exception as e:
        print(f"❌ Error testing direct retriever: {e}")

if __name__ == '__main__':
    # Path to test PDF file
    input_file = Path(__file__).parent.parent.parent / 'preprocessors' / 'examples' / 'input_dir' / 'cau-hinh-cho-mot-network-load-balancer.pdf'
    print("Testing Preprocessed PDF Retriever:")
    print("-" * 50)
    test_preprocessed_retriever(input_file)
    
    # print("\nTesting Direct PDF Retriever:")
    # print("-" * 50)
    # test_direct_retriever(input_file)