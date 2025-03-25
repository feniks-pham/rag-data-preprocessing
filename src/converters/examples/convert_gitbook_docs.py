from pathlib import Path
from src.converters.gitbook_markdown_converter import GitBookMarkdownConverter

def main():
    # Initialize the converter
    converter = GitBookMarkdownConverter()
    
    # Define input and output paths
    input_folder = Path("./data/vngcloud_docs")
    output_folder = Path("./preprocessed_docs/vngcloud_docs")
    
    # Get all markdown files recursively
    markdown_files = list(input_folder.rglob("*.md"))
    
    # Convert all files
    converted_files = converter.convert_batch(markdown_files, output_folder)
    
    # Print summary
    print(f"🎉 Markdown conversion completed for {len(converted_files)} files.")
    print("\nConverted files:")
    for file in converted_files:
        print(f"✅ {file}")

if __name__ == "__main__":
    main() 