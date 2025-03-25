import base64
import re
from pathlib import Path
from typing import Union, List

import requests
from bs4 import BeautifulSoup

from .base_converter import BaseConverter
from ..utils.file_utils import ensure_dir, get_output_path, read_file_content, write_file_content
from ..utils.regex_utils import (
    convert_relative_links,
    convert_html_table,
    convert_gitbook_hints,
    convert_images,
    clean_markdown,
    HTML_TABLE_PATTERN
)


class GitBookMarkdownConverter(BaseConverter):
    """Converter for GitBook markdown to pure Markdown format."""
    
    def __init__(self, github_assets_base_url: str = None):
        """
        Initialize the converter.
        
        Args:
            github_assets_base_url: Base URL for GitHub assets. If None, will use default VNG docs URL.
        """
        self.github_assets_base_url = github_assets_base_url or "https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets"

    def _download_and_encode_image(self, url: str) -> str:
        """Download an image from a URL and encode it as base64."""
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            img_base64 = base64.b64encode(response.content).decode("utf-8")
            return f"![Image](data:image/png;base64,{img_base64})"
        return f"![Failed to load]({url})"

    def _process_html_tag(self, tag) -> str:
        """Convert individual HTML elements to Markdown format."""
        # Process strong tags
        for strong in tag.find_all("strong"):
            strong.insert_before(f"**{strong.text.strip()}**")
            strong.decompose()

        # Process code tags
        for code in tag.find_all("code"):
            code.insert_before(f"{code.text.strip()}")
            code.decompose()

        # Process anchor tags
        for a in tag.find_all("a"):
            link_text = a.text.strip()
            link_href = a.get("href", "#")
            a.insert_before(f"[{link_text}]({link_href})")
            a.decompose()

        return tag.get_text(separator=" ").strip()

    def _convert_html_to_markdown(self, tag) -> str:
        """Convert an HTML fragment to Markdown while preserving lists, bold text, and links."""
        markdown_text = []
        
        # Process unordered lists
        for ul in tag.find_all("ul"):
            for li in ul.find_all("li"):
                text = self._process_html_tag(li)
                markdown_text.append(f"- {text}")
            ul.decompose()

        # Process remaining text
        remaining_text = self._process_html_tag(tag)
        if remaining_text:
            markdown_text.append(remaining_text)

        return " <br> ".join(markdown_text).strip()

    def _convert_html_table_to_markdown(self, html: str) -> str:
        """Convert an HTML table to Markdown format."""
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table")
        if not table:
            return ""

        # Extract headers
        headers = [th.text.strip() for th in table.find_all("th")]
        if not headers:
            return ""

        # Create table structure
        header_row = "| " + " | ".join(headers) + " |"
        separator = "| " + " | ".join(["---"] * len(headers)) + " |"

        # Extract and convert rows
        rows = []
        for tr in table.find_all("tr")[1:]:
            row_data = [self._convert_html_to_markdown(td) for td in tr.find_all("td")]
            rows.append("| " + " | ".join(row_data) + " |")

        return "\n".join([header_row, separator] + rows)

    def _process_markdown(self, md_text: str, md_file_path: Union[str, Path]) -> str:
        """Convert GitBook Markdown with HTML elements to pure Markdown."""
        # Convert images
        md_text = convert_images(md_text, self.github_assets_base_url)
        
        # Convert HTML tables
        md_text = re.sub(HTML_TABLE_PATTERN, 
                        lambda m: convert_html_table(m.group(0)), 
                        md_text, flags=re.DOTALL)
        
        # Convert GitBook hints
        md_text = convert_gitbook_hints(md_text)
        
        # Convert relative links
        md_text = convert_relative_links(md_text, str(md_file_path))
        
        # Clean up markdown
        md_text = clean_markdown(md_text)
        
        return md_text

    def convert_to_markdown(self, input_path: Union[str, Path], output_path: Union[str, Path] = None) -> str:
        """
        Convert a GitBook Markdown file to pure Markdown.
        
        Args:
            input_path: Path to the input GitBook Markdown file
            output_path: Optional path to save the converted Markdown
            
        Returns:
            str: The converted Markdown content if output_path is None
        """
        input_path = Path(input_path)
        
        if not input_path.suffix.lower() == '.md':
            raise ValueError("Input file must be a markdown file")
            
        # Read input file
        markdown_content = read_file_content(input_path)
        
        # Convert content
        converted_content = self._process_markdown(markdown_content, input_path)
        
        if output_path:
            write_file_content(output_path, converted_content)
            return ""
            
        return converted_content

    def convert_batch(self, input_paths: List[Union[str, Path]], output_dir: Union[str, Path]) -> List[Path]:
        """
        Convert multiple GitBook markdown files to pure markdown.
        
        Args:
            input_paths: List of paths to GitBook markdown files
            output_dir: Directory to save the converted files
            
        Returns:
            List[Path]: List of paths to the converted files
        """
        output_dir = ensure_dir(output_dir)
        converted_files = []
        
        for input_path in input_paths:
            input_path = Path(input_path)
            if input_path.suffix.lower() == '.md':
                output_path = get_output_path(input_path, output_dir)
                self.convert_to_markdown(input_path, output_path)
                converted_files.append(output_path)
                
        return converted_files 