from pathlib import Path
from typing import Union, List, Generator
import os
import shutil

def ensure_dir(dir_path: Union[str, Path]) -> Path:
    """
    Create directory if it doesn't exist.
    
    Args:
        dir_path: Path to directory
        
    Returns:
        Path: Path object of the directory
    """
    dir_path = Path(dir_path)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path

def get_output_path(input_path: Union[str, Path], output_dir: Union[str, Path], extension: str = '.md') -> Path:
    """
    Generate output file path from input path.
    
    Args:
        input_path: Path to input file
        output_dir: Directory for output file
        extension: File extension for output file (default: .md)
        
    Returns:
        Path: Output file path
    """
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    return output_dir / f"{input_path.stem}{extension}"

def find_files(
    directory: Union[str, Path], 
    pattern: str = "*", 
    recursive: bool = True
) -> Generator[Path, None, None]:
    """
    Find files matching pattern in directory.
    
    Args:
        directory: Directory to search in
        pattern: Glob pattern to match files (default: "*")
        recursive: Whether to search recursively (default: True)
        
    Yields:
        Path: Matching file paths
    """
    directory = Path(directory)
    if recursive:
        yield from directory.rglob(pattern)
    else:
        yield from directory.glob(pattern)

def copy_directory_structure(
    src_dir: Union[str, Path], 
    dst_dir: Union[str, Path], 
    ignore_patterns: List[str] = None
) -> None:
    """
    Copy directory structure while preserving hierarchy.
    
    Args:
        src_dir: Source directory
        dst_dir: Destination directory
        ignore_patterns: List of patterns to ignore (default: None)
    """
    src_dir = Path(src_dir)
    dst_dir = Path(dst_dir)
    
    if ignore_patterns is None:
        ignore_patterns = []
        
    def ignore_func(dir_path, contents):
        ignored = []
        for pattern in ignore_patterns:
            ignored.extend([c for c in contents if Path(dir_path) / c == pattern])
        return ignored
    
    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True, ignore=ignore_func)

def read_file_content(file_path: Union[str, Path], encoding: str = 'utf-8') -> str:
    """
    Read file content with proper encoding handling.
    
    Args:
        file_path: Path to file
        encoding: File encoding (default: utf-8)
        
    Returns:
        str: File content
    """
    file_path = Path(file_path)
    try:
        return file_path.read_text(encoding=encoding)
    except UnicodeDecodeError:
        # Try different encodings if utf-8 fails
        encodings = ['latin1', 'cp1252', 'iso-8859-1']
        for enc in encodings:
            try:
                return file_path.read_text(encoding=enc)
            except UnicodeDecodeError:
                continue
        raise ValueError(f"Could not read file {file_path} with any supported encoding")

def write_file_content(
    file_path: Union[str, Path], 
    content: str, 
    encoding: str = 'utf-8',
    create_dirs: bool = True
) -> None:
    """
    Write content to file with proper directory creation.
    
    Args:
        file_path: Path to file
        content: Content to write
        encoding: File encoding (default: utf-8)
        create_dirs: Whether to create parent directories (default: True)
    """
    file_path = Path(file_path)
    if create_dirs:
        file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding=encoding)

def get_relative_path(path: Union[str, Path], base_path: Union[str, Path]) -> Path:
    """
    Get relative path from base path.
    
    Args:
        path: Path to get relative path for
        base_path: Base path to calculate relative path from
        
    Returns:
        Path: Relative path
    """
    return Path(path).relative_to(Path(base_path))
