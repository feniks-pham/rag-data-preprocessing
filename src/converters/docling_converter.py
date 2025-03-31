from abc import ABC
from typing import Union

from docling.document_converter import DocumentConverter
from pathlib import Path

from src.converters.base_converter import BaseConverter


class DoclingConverter(BaseConverter, ABC):
    """Converter for HTML, DOCX, and properly formatted PDFs using docling."""
    
    SUPPORTED_FORMATS = ['.html', '.docx', '.pdf']
    
    def __init__(self):
        self.converter = DocumentConverter()
    
    def convert_to_markdown(self, input_path: Union[str, Path], output_path: Union[str, Path] = None) -> str:
        """Convert a single document to markdown."""
        input_path = Path(input_path)
        
        if input_path.suffix.lower() not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported file format: {input_path.suffix}. Supported formats: {self.SUPPORTED_FORMATS}")
        
        markdown_content = self.converter.convert_to_markdown(str(input_path))
        
        if output_path:
            output_path = Path(output_path)
            output_path.write_text(markdown_content, encoding='utf-8')
            return ""
        
        return markdown_content
    
    # def convert_batch(self, input_paths: List[Union[str, Path]], output_dir: Union[str, Path]) -> List[Path]:
    #     """Convert multiple documents to markdown."""
    #     output_dir = _ensure_output_dir(output_dir)
    #     converted_files = []
    #
    #     for input_path in input_paths:
    #         input_path = Path(input_path)
    #         if input_path.suffix.lower() in self.SUPPORTED_FORMATS:
    #             output_path = _get_output_path(input_path, output_dir)
    #             self.convert_to_markdown(input_path, output_path)
    #             converted_files.append(output_path)
    #
    #     return converted_files
