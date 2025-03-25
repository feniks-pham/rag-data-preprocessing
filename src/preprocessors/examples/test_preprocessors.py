from pathlib import Path
from src.preprocessors.pdf_preprocessor import PDFPreprocessor
from src.preprocessors.html_crawler_preprocessor import HTMLCrawlerPreprocessor

def test_pdf_preprocessor():
    """Test the PDF preprocessor with a sample PDF file."""
    # Initialize preprocessor
    preprocessor = PDFPreprocessor()
    
    # Path to test PDF file
    # input_file = Path(__file__).parent / 'input_dir' / 'cau-hinh-cho-mot-network-load-balancer.pdf'
    #
    # # Process single file
    # try:
    #     output_file = preprocessor.process_pdf(input_file)
    #     print(f"✅ Successfully processed {input_file} to {output_file}")
    # except Exception as e:
    #     print(f"❌ Error processing single file: {e}")
    
    # Process directory
    input_dir = Path(__file__).parent / 'input_dir'
    output_dir = Path(__file__).parent / 'output_dir'

    try:
        output_files = preprocessor.process_directory(input_dir, output_dir)
        print(f"✅ Successfully processed {len(output_files)} files from directory")
        for file in output_files:
            print(f"  - {file}")
    except Exception as e:
        print(f"❌ Error processing directory: {e}")

def test_html_crawler():
    """Test the HTML crawler with a sample domain."""
    # Initialize crawler with base URL
    base_url = "https://example.com"  # Replace with actual domain
    crawler = HTMLCrawlerPreprocessor(base_url)
    
    # Set output directory for HTML files
    output_dir = Path(__file__).parent / 'crawled_html'
    
    try:
        # Crawl domain with max 10 pages
        output_files = crawler.crawl_domain(output_dir, max_pages=10)
        print(f"✅ Successfully crawled and saved {len(output_files)} HTML files:")
        for file in output_files:
            print(f"  - {file}")
    except Exception as e:
        print(f"❌ Error during crawling: {e}")

if __name__ == '__main__':
    print("Testing PDF Preprocessor:")
    print("-" * 50)
    test_pdf_preprocessor()
    
    # print("\nTesting HTML Crawler:")
    # print("-" * 50)
    # test_html_crawler()