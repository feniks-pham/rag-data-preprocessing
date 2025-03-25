from pathlib import Path
from src.converters.markdown_to_pdf_converter import MarkdownToPDFConverter

def convert_one_file():
    input_file = Path(__file__).parent / 'test.md'
    output_file = Path(__file__).parent / 'test.pdf'
    converter = MarkdownToPDFConverter()
    converter.convert_to_pdf(input_file, output_file)

def main():
    # Khởi tạo converter
    converter = MarkdownToPDFConverter()
    
    # Đường dẫn đến thư mục chứa các file markdown
    input_dir = Path(__file__).parent / 'input_dir'
    
    # Đường dẫn để lưu các file PDF
    output_dir = Path(__file__).parent / 'output_dir'
    
    # Lấy danh sách tất cả các file markdown trong thư mục input
    markdown_files = list(input_dir.glob('**/*.md'))
    
    if not markdown_files:
        print("Không tìm thấy file markdown nào trong thư mục input_dir")
        return
    
    # Thực hiện chuyển đổi hàng loạt
    output_files = converter.convert_batch(markdown_files, output_dir)
    
    print(f"Đã chuyển đổi {len(output_files)} file markdown thành PDF:")
    for output_file in output_files:
        print(f"- {output_file}")


if __name__ == '__main__':
    # main() 
    convert_one_file()