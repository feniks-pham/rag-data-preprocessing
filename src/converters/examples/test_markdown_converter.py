from pathlib import Path
from src.converters.markdown_to_pdf_converter import MarkdownToPDFConverter

def convert_one_file():
    input_file = Path(__file__).parent / 'test.md'
    output_file = Path(__file__).parent / 'test.pdf'
    converter = MarkdownToPDFConverter()
    converter.convert_to_pdf(input_file, output_file)

def main():
    # Initialize converter
    converter = MarkdownToPDFConverter()
    
    # Path to directory containing markdown files
    input_dir = Path(__file__).parent / 'input_dir'
    
    # Path to save PDF files
    output_dir = Path(__file__).parent / 'output_dir'
    
    # Get list of all markdown files in input directory
    markdown_files = list(input_dir.glob('**/*.md'))
    
    if not markdown_files:
        print("No markdown files found in input_dir")
        return
    
    # Perform batch conversion
    output_files = converter.convert_batch(markdown_files, output_dir)
    
    print(f"Converted {len(output_files)} markdown files to PDF:")
    for output_file in output_files:
        print(f"- {output_file}")


if __name__ == '__main__':
    # main() 
    convert_one_file()