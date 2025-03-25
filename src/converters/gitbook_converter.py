from pathlib import Path
from typing import Union, List

from base_converter import BaseConverter
from src.utils.file_utils import ensure_dir, get_output_path


class GitBookConverter(BaseConverter):
    """Converter for GitBook documentation to markdown."""
    
    def __init__(self):
        self.summary_file = "SUMMARY.md"
        self.config_file = "book.json"
    
    def _parse_summary(self, summary_content: str) -> List[dict]:
        """Parse SUMMARY.md to get the structure of the GitBook."""
        pages = []
        for line in summary_content.split('\n'):
            if line.strip().startswith('*') or line.strip().startswith('-'):
                # Extract markdown link format: [Title](path/to/file.md)
                parts = line.strip()[1:].strip().split('](')
                if len(parts) == 2:
                    title = parts[0][1:]  # Remove leading [
                    path = parts[1][:-1]  # Remove trailing )
                    pages.append({
                        'title': title,
                        'path': path
                    })
        return pages
    
    def convert_to_markdown(self, input_path: Union[str, Path], output_path: Union[str, Path] = None) -> str:
        """
        Convert a GitBook directory to markdown.
        
        Args:
            input_path: Path to the GitBook directory
            output_path: Optional path to save the combined markdown output
        """
        input_path = Path(input_path)
        if not input_path.is_dir():
            raise ValueError("Input path must be a GitBook directory")
        
        # Read SUMMARY.md to get the structure
        summary_path = input_path / self.summary_file
        if not summary_path.exists():
            raise ValueError(f"Could not find {self.summary_file} in GitBook directory")
        
        summary_content = summary_path.read_text(encoding='utf-8')
        pages = self._parse_summary(summary_content)
        
        # Combine all markdown files
        combined_content = []
        for page in pages:
            page_path = input_path / page['path']
            if page_path.exists():
                content = page_path.read_text(encoding='utf-8')
                combined_content.append(f"# {page['title']}\n\n{content}\n\n")
        
        markdown_content = '\n'.join(combined_content)
        
        if output_path:
            output_path = Path(output_path)
            output_path.write_text(markdown_content, encoding='utf-8')
            return ""
        
        return markdown_content
    
    def convert_batch(self, input_paths: List[Union[str, Path]], output_dir: Union[str, Path]) -> List[Path]:
        """
        Convert multiple GitBook directories to markdown.
        
        Args:
            input_paths: List of paths to GitBook directories
            output_dir: Directory to save the markdown outputs
        """
        output_dir = ensure_dir(output_dir)
        converted_files = []
        
        for input_path in input_paths:
            input_path = Path(input_path)
            if input_path.is_dir():
                output_path = get_output_path(input_path, output_dir)
                self.convert_to_markdown(input_path, output_path)
                converted_files.append(output_path)
        
        return converted_files
