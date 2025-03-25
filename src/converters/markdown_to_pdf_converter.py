import os
import tempfile
from pathlib import Path
from typing import Union, List

import markdown
from bs4 import BeautifulSoup

from .html_to_pdf_converter import HTMLToPDFConverter


class MarkdownToPDFConverter:
    """Converter for Markdown to PDF conversion using markdown and HTMLToPDFConverter."""
    
    def __init__(self, wkhtmltopdf_path: str = None):
        """
        Initialize the converter.
        
        Args:
            wkhtmltopdf_path: Path to wkhtmltopdf executable. If None, will try to use system default.
        """
        self.html_converter = HTMLToPDFConverter(wkhtmltopdf_path)
        self.md = markdown.Markdown(extensions=[
            'tables',
            'fenced_code',
            'codehilite',
            'extra'
        ])

    def _process_markdown(self, markdown_content: str) -> str:
        """Process markdown content to handle relative image paths."""
        # First convert markdown to HTML
        html_content = self.md.convert(markdown_content)
        
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Process all images in the HTML
        for img in soup.find_all('img'):
            if img.get('src'):
                src = img['src']
                # Convert GitHub URL if needed
                if 'github.com' in src and '/tree/' in src:
                    src = src.replace('/tree/', '/raw/')
                # Update the image source
                img['src'] = src
        
        return str(soup)

    def convert_to_pdf(self, input_path: Union[str, Path], output_path: Union[str, Path] = None) -> str:
        """
        Convert Markdown to PDF format.
        
        Args:
            input_path: Path to the input Markdown file
            output_path: Optional path to save the PDF output. If not provided, 
                        will return the PDF content as bytes
        
        Returns:
            bytes: The PDF content if output_path is None, otherwise returns empty string
        """
        input_path = Path(input_path)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        # Read markdown content
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Process markdown content
        processed_content = self._process_markdown(markdown_content)
        
        # Create complete HTML document
        html_doc = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                img {{
                    max-width: 100%;
                    height: auto;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 1em 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f5f5f5;
                }}
                pre {{
                    background-color: #f5f5f5;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
                code {{
                    font-family: Consolas, monospace;
                }}
                figure {{
                    margin: 1em 0;
                }}
                figcaption {{
                    text-align: center;
                    font-style: italic;
                    color: #666;
                }}
            </style>
        </head>
        <body>
            {processed_content}
        </body>
        </html>
        """
        
        # Create a temporary HTML file
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False, mode='w', encoding='utf-8') as temp_html:
            temp_html.write(html_doc)
            temp_html_path = temp_html.name
        
        try:
            # Convert HTML to PDF
            if output_path:
                output_path = Path(output_path)
                self.html_converter.convert_to_markdown(temp_html_path, output_path)
                return ""
            else:
                return self.html_converter.convert_to_markdown(temp_html_path)
        finally:
            # Clean up temporary file
            os.unlink(temp_html_path)

    def convert_batch(self, input_paths: List[Union[str, Path]], output_dir: Union[str, Path]) -> List[Path]:
        """
        Convert multiple Markdown files to PDF format.
        
        Args:
            input_paths: List of paths to input Markdown files
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
            self.convert_to_pdf(input_path, output_path)
            output_files.append(output_path)
            
        return output_files 