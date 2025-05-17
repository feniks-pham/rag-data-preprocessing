from src.retrievers.direct_pdf_retriever import DirectPDFRetriever
from src.retrievers.html_retriever import HTMLRetriever
from src.retrievers.preprocessed_pdf_retriever import PreprocessedPDFRetriever


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


def test_html_retriever(test_urls):
    """Test the HTMLRetriever."""
    # Initialize retriever with small max_pages and max_depth for testing
    retriever = HTMLRetriever(
        collection_name="test_html",
        chunk_size=1000,
        chunk_overlap=200,
        max_pages=2,  # Limit pages for testing
        max_depth=1   # Limit depth for testing
    )
    
    # Add documents
    retriever.add_documents(test_urls)
    
    # Test retrieval
    results = retriever.get_relevant_documents("test query")
    assert len(results) > 0
    assert all(hasattr(doc, 'page_content') for doc in results)
    assert all(hasattr(doc, 'metadata') for doc in results)
    
    # Test metadata
    for doc in results:
        assert 'source' in doc.metadata
        assert 'chunk_index' in doc.metadata
        assert 'document_id' in doc.metadata
        assert doc.metadata['source'] in test_urls

# def test_html_retriever_error_handling():
#     """Test error handling in HTMLRetriever."""
#     # Initialize retriever
#     retriever = HTMLRetriever(
#         collection_name="test_html_errors",
#         max_pages=1,
#         max_depth=1
#     )
#
#     # Test with invalid URL
#     invalid_urls = [
#         "https://this-is-not-a-real-domain.com",
#         "not-a-url"
#     ]
#
#     # Should handle errors gracefully
#     retriever.add_documents(invalid_urls)
#
#     # Test retrieval with empty collection
#     results = retriever.get_relevant_documents("test query")
#     assert isinstance(results, list)
#     assert len(results) == 0
#
# def test_html_retriever_content_cleaning():
#     """Test HTML content cleaning in HTMLRetriever."""
#     # Initialize retriever
#     retriever = HTMLRetriever(
#         collection_name="test_html_cleaning",
#         max_pages=1,
#         max_depth=1
#     )
#
#     # Test with a simple HTML page
#     test_url = "https://example.com"
#
#     # Process URL
#     chunks = retriever._process_and_split_document(test_url)
#
#     # Check content cleaning
#     if chunks:
#         content = chunks[0].page_content
#         # Content should not contain HTML tags
#         assert '<' not in content
#         assert '>' not in content
#         # Content should not contain script or style content
#         assert 'script' not in content.lower()
#         assert 'style' not in content.lower()
#         # Content should be non-empty
#         assert len(content.strip()) > 0
#
# def test_html_retriever_chunking():
#     """Test document chunking in HTMLRetriever."""
#     # Initialize retriever with small chunk size
#     retriever = HTMLRetriever(
#         collection_name="test_html_chunking",
#         chunk_size=500,  # Small chunk size for testing
#         chunk_overlap=100,
#         max_pages=1,
#         max_depth=1
#     )
#
#     # Test with a content-rich page
#     test_url = "https://example.com"
#
#     # Process URL
#     chunks = retriever._process_and_split_document(test_url)
#
#     # Check chunking
#     if len(chunks) > 1:
#         # Check chunk sizes
#         for chunk in chunks:
#             assert len(chunk.page_content) <= retriever.chunk_size
#         # Check overlap
#         for i in range(len(chunks) - 1):
#             overlap = set(chunks[i].page_content.split()) & set(chunks[i + 1].page_content.split())
#             assert len(overlap) >= retriever.chunk_overlap // 10  # Approximate word overlap

if __name__ == '__main__':
    # Path to test PDF file
    # input_file = Path(__file__).parent.parent.parent / 'preprocessors' / 'examples' / 'input_dir' / 'cau-hinh-cho-mot-network-load-balancer.pdf'
    # print("Testing Preprocessed PDF Retriever:")
    # print("-" * 50)
    # test_preprocessed_retriever(input_file)
    #
    # print("\nTesting Direct PDF Retriever:")
    # print("-" * 50)
    # test_direct_retriever(input_file)

    # Test URLs (using a simple, reliable website)
    test_urls = [
        "https://vngcloud.vn/en/product/vdb",  # Simple test page
    ]
    print("\Testing HTML Retriever:")
    print("-" * 50)
    test_html_retriever(test_urls)