from pathlib import Path
from typing import Union, List
from markitdown import MarkItDown

from src.converters.base_converter import BaseConverter

md = MarkItDown()

class MarkitdownConverter(BaseConverter):
    """Converter for problematic PDFs using markitdown."""
    
    def __init__(self, ocr_enabled: bool = True):
        """
        Initialize the converter.
        
        Args:
            ocr_enabled: Whether to use OCR for scanned PDFs
        """
        self.converter = markitdown.PDFConverter(ocr_enabled=ocr_enabled)
    
    def convert_to_markdown(self, input_path: Union[str, Path], output_path: Union[str, Path] = None) -> str:
        """Convert a single PDF to markdown."""
        input_path = Path(input_path)
        
        if input_path.suffix.lower() != '.pdf':
            raise ValueError("MarkitdownConverter only supports PDF files")
        
        markdown_content = self.converter.convert_pdf(str(input_path))
        
        if output_path:
            output_path = Path(output_path)
            output_path.write_text(markdown_content, encoding='utf-8')
            return ""
        
        return markdown_content
    
    # def convert_batch(self, input_paths: List[Union[str, Path]], output_dir: Union[str, Path]) -> List[Path]:
    #     """Convert multiple PDFs to markdown."""
    #     output_dir = _ensure_output_dir(output_dir)
    #     converted_files = []
    #
    #     for input_path in input_paths:
    #         input_path = Path(input_path)
    #         if input_path.suffix.lower() == '.pdf':
    #             output_path = _get_output_path(input_path, output_dir)
    #             self.convert_to_markdown(input_path, output_path)
    #             converted_files.append(output_path)
    #
    #     return converted_files
