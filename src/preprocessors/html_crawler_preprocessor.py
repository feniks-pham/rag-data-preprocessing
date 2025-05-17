from typing import Optional
from urllib.parse import urlparse

import requests
import scrapy
from bs4 import BeautifulSoup
from pathlib import Path
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class WebSpider(scrapy.Spider):
    """Scrapy spider for crawling web content."""
    
    name = 'web_spider'
    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS': 1,
    }
    
    def __init__(self, url: str, output_file: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]
        self.output_file = output_file
        self.content = None  # Chỉ lưu nội dung trang đầu tiên
        
    def parse(self, response):
        """Parse the response and extract content."""
        # Chỉ lưu nội dung trang đầu tiên
        if self.content is None:
            self.content = response.text
            
        # Follow links within the same domain
        domain = urlparse(response.url).netloc
        for href in response.css('a::attr(href)').getall():
            if href.startswith('/') or urlparse(href).netloc == domain:
                yield response.follow(href, self.parse)
    
    def closed(self, reason):
        """Save content when spider is closed."""
        if self.content:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(self.content)  # Lưu trực tiếp nội dung HTML


class HTMLCrawlerPreprocessor:
    """Preprocessor for crawling and cleaning web content."""
    
    def __init__(self, max_pages: int = 10, max_depth: int = 2):
        """
        Initialize the HTML crawler preprocessor.
        
        Args:
            max_pages: Maximum number of pages to crawl
            max_depth: Maximum depth of crawling
        """
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.process = None
    
    def _clean_html(self, html_content: str) -> str:
        """
        Clean HTML content using BeautifulSoup while preserving all text content.
        
        Args:
            html_content: Raw HTML content
            
        Returns:
            str: Cleaned text content with HTML tags removed
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Get all text content, including from scripts and styles
        text = soup.get_text(separator='\n', strip=True)

        script_content = "\n\n".join(script.get_text() for script in soup.find_all("script"))

        # Kết hợp cả hai nội dung
        text = text + "\n" + script_content
        
        # Clean up whitespace but preserve line breaks
        lines = []
        for line in text.split('\n'):
            line = line.strip()
            if line:
                # Remove multiple spaces but preserve single spaces
                line = ' '.join(line.split())
                lines.append(line)
        
        # Join lines with double newlines for better readability
        return '\n\n'.join(lines)
    
    def _crawl_with_scrapy(self, url: str, output_file: str) -> bool:
        """
        Crawl website using Scrapy.
        
        Args:
            url: URL to crawl
            output_file: Path to save crawled content
            
        Returns:
            bool: True if crawling was successful
        """
        try:
            # Configure Scrapy settings
            settings = get_project_settings()
            settings.update({
                'CLOSESPIDER_PAGECOUNT': self.max_pages,
                'CLOSESPIDER_DEPTH': self.max_depth,
                'LOG_LEVEL': 'ERROR'
            })
            
            # Create and run spider
            process = CrawlerProcess(settings)
            process.crawl(WebSpider, url=url, output_file=output_file)
            process.start()
            return True
        except Exception as e:
            print(f"❌ Error crawling with Scrapy: {e}")
            return False
    
    def _crawl_with_requests(self, url: str, output_file: str) -> bool:
        """
        Crawl website using requests (fallback method).
        
        Args:
            url: URL to crawl
            output_file: Path to save crawled content
            
        Returns:
            bool: True if crawling was successful
        """
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Clean and save content
            cleaned_content = self._clean_html(response.text)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            return True
        except Exception as e:
            print(f"❌ Error crawling with requests: {e}")
            return False
    
    def process_url(self, url: str) -> Optional[str]:
        """
        Process a URL and return cleaned content.
        
        Args:
            url: URL to process
            
        Returns:
            Optional[str]: Path to the processed content file, or None if processing failed
        """
        try:
            print(f"🔄 Processing URL: {url}")
            
            # Create output directory if it doesn't exist
            output_dir = Path('output_dir')
            output_dir.mkdir(exist_ok=True)
            
            # Generate output file path
            output_file = output_dir / f"{urlparse(url).netloc}.html"
            
            # Try Scrapy first
            if self._crawl_with_scrapy(url, str(output_file)):
                print(f"✅ Successfully crawled with Scrapy: {url}")
            else:
                print("⚠️ Scrapy failed, trying requests...")
                if not self._crawl_with_requests(url, str(output_file)):
                    print("❌ Both crawling methods failed")
                    return None
            
            # Clean the crawled content
            with open(output_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            cleaned_content = self._clean_html(html_content)
            
            # Save cleaned content
            md_file = output_file.with_suffix('.md')
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            
            print(f"✅ Successfully processed URL: {url}")
            return str(md_file)
            
        except Exception as e:
            print(f"❌ Error processing URL {url}: {str(e)}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            return None 