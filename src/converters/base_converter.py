from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union, List


class BaseConverter(ABC):
    """Base class for all document converters."""
    
    @abstractmethod
    def convert_to_markdown(self, input_path: Union[str, Path], output_path: Union[str, Path] = None) -> str:
        """
        Convert a document to Markdown format.
        
        Args:
            input_path: Path to the input document
            output_path: Optional path to save the markdown output. If not provided, 
                        will return the markdown content as string
        
        Returns:
            str: The markdown content if output_path is None, otherwise returns empty string
        """
        pass

    @abstractmethod
    def convert_batch(self, input_paths: List[Union[str, Path]], output_dir: Union[str, Path]) -> List[Path]:
        """
        Convert multiple documents to Markdown format.
        
        Args:
            input_paths: List of paths to input documents
            output_dir: Directory to save the markdown outputs
            
        Returns:
            List[Path]: List of paths to the generated markdown files
        """
        pass
