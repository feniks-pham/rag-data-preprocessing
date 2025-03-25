import hashlib
import os
from pathlib import Path
from typing import Union, List
from urllib.parse import urljoin, urlparse

import pdfkit
import requests
from bs4 import BeautifulSoup

from .base_converter import BaseConverter


class HTMLToPDFConverter(BaseConverter):
    """Converter for HTML to PDF conversion using pdfkit and wkhtmltopdf."""
    
    def __init__(self, wkhtmltopdf_path: str = None):
        """
        Initialize the converter.
        
        Args:
            wkhtmltopdf_path: Path to wkhtmltopdf executable. If None, will try to use system default.
        """
        self.config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path) if wkhtmltopdf_path else None
        self.options = {
            'encoding': 'UTF-8',
            'page-size': 'A4',
            'margin-top': '20mm',
            'margin-right': '20mm',
            'margin-bottom': '20mm',
            'margin-left': '20mm',
            'enable-local-file-access': True,
            'quiet': True,
            'dpi': 300,
            'orientation': 'Portrait',
            'custom-header': [
                ('Accept-Encoding', 'gzip'),
                ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
            ]
        }

    def _convert_github_url(self, url: str) -> str:
        """Convert GitHub URL to raw content URL."""
        # Convert GitHub URL to raw content URL
        if 'github.com' in url and '/tree/' in url:
            url = url.replace('/tree/', '/raw/')
        return url

    def _get_safe_filename(self, url: str) -> str:
        """Generate a safe filename from URL."""
        # Create a hash of the URL
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        
        # Get file extension from URL or default to .png
        ext = os.path.splitext(urlparse(url).path)[1]
        if not ext:
            ext = '.png'
        
        # Create a safe filename
        return f"img_{url_hash}{ext}"

    def _download_resource(self, url: str, resource_dir: Path) -> str:
        """Download a resource and return its local path."""
        try:
            # Convert GitHub URL if needed
            url = self._convert_github_url(url)
            
            # Add headers to mimic browser request
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Referer': 'https://github.com/'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                # Generate a safe filename
                safe_filename = self._get_safe_filename(url)
                local_path = resource_dir / safe_filename
                
                with open(local_path, 'wb') as f:
                    f.write(response.content)
                return str(local_path)
            else:
                print(f"Failed to download {url}: Status code {response.status_code}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")
        return url

    def _process_html(self, html_content: str, resource_dir: Path) -> str:
        """Process HTML content to download and update resource references."""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Add default styles
        style_tag = soup.new_tag('style')
        style_tag.string = '''
            body { 
                font-family: Arial, sans-serif;
                font-size: 12pt;
                line-height: 1.6;
                max-width: 100%;
                margin: 0 auto;
                padding: 20px;
            }
            table { 
                border-collapse: collapse;
                width: 100%;
                margin: 1em 0;
                font-size: 11pt;
                table-layout: fixed;
            }
            tr { 
                page-break-inside: avoid;
                page-break-after: auto;
            }
            thead { 
                display: table-header-group;
            }
            tfoot { 
                display: table-row-group;
            }
            th, td { 
                border: 1px solid #ddd;
                padding: 12px 8px;
                text-align: left;
                word-wrap: break-word;
                overflow-wrap: break-word;
                hyphens: auto;
                min-width: 100px;
                vertical-align: top;
            }
            th { 
                background-color: #f2f2f2;
                font-weight: bold;
            }
            pre { 
                background-color: #f5f5f5;
                padding: 15px;
                border-radius: 5px;
                white-space: pre-wrap;
                word-wrap: break-word;
                font-size: 10pt;
            }
            code { 
                font-family: Consolas, monospace;
                font-size: 10pt;
            }
            img { 
                max-width: 100%;
                height: auto;
                display: block;
                margin: 1em auto;
                page-break-inside: avoid;
            }
            figure {
                margin: 1em 0;
                text-align: center;
                page-break-inside: avoid;
            }
            figcaption {
                text-align: center;
                font-style: italic;
                color: #666;
                margin-top: 0.5em;
            }
            h1, h2, h3, h4, h5, h6 {
                page-break-after: avoid;
            }
            p {
                margin: 1em 0;
            }
            /* Thêm CSS cho bảng responsive */
            @media screen and (max-width: 600px) {
                table {
                    display: block;
                    overflow-x: auto;
                }
            }
        '''
        soup.head.append(style_tag)
        
        # Process CSS files
        for link in soup.find_all('link', rel='stylesheet'):
            if link.get('href'):
                url = urljoin(link['href'], link['href'])
                local_path = self._download_resource(url, resource_dir)
                link['href'] = local_path
        
        # Process JavaScript files
        for script in soup.find_all('script', src=True):
            url = urljoin(script['src'], script['src'])
            local_path = self._download_resource(url, resource_dir)
            script['src'] = local_path
        
        # Process images
        for img in soup.find_all('img'):
            if img.get('src'):
                url = urljoin(img['src'], img['src'])
                local_path = self._download_resource(url, resource_dir)
                img['src'] = local_path
                # Add alt text if missing
                if not img.get('alt'):
                    img['alt'] = 'Image'
        
        return str(soup)

    def convert_to_markdown(self, input_path: Union[str, Path], output_path: Union[str, Path] = None) -> str:
        """
        Convert HTML to PDF format.
        
        Args:
            input_path: Path to the input HTML file
            output_path: Optional path to save the PDF output. If not provided, 
                        will return the PDF content as bytes
        
        Returns:
            bytes: The PDF content if output_path is None, otherwise returns empty string
        """
        input_path = Path(input_path)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        # Create resource directory
        resource_dir = input_path.parent / 'resources'
        resource_dir.mkdir(exist_ok=True)
        
        # Read and process HTML
        with open(input_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        processed_html = self._process_html(html_content, resource_dir)
        
        # Save processed HTML
        processed_html_path = input_path.parent / 'processed.html'
        with open(processed_html_path, 'w', encoding='utf-8') as f:
            f.write(processed_html)
            
        if output_path:
            output_path = Path(output_path)
            pdfkit.from_file(str(processed_html_path), str(output_path), 
                           configuration=self.config, options=self.options)
            return ""
        else:
            return pdfkit.from_file(str(processed_html_path), False, 
                                  configuration=self.config, options=self.options)

    def convert_batch(self, input_paths: List[Union[str, Path]], output_dir: Union[str, Path]) -> List[Path]:
        """
        Convert multiple HTML files to PDF format.
        
        Args:
            input_paths: List of paths to input HTML files
            output_dir: Directory to save the PDF outputs
            
        Returns:
            List[Path]: List of paths to the generated PDF files
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_files = []
        for input_path in input_paths:
            input_path = Path(input_path)
            output_path = output_dir / f"{input_path.stem}.pdf"
            self.convert_to_markdown(input_path, output_path)
            output_files.append(output_path)
            
        return output_files 