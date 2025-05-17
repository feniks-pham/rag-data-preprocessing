import os
from pathlib import Path
import sys

# Thêm đường dẫn của project vào PYTHONPATH
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

# Import từ src.converters thay vì converters
from src.converters.html_to_pdf_converter import HTMLToPDFConverter

def main():
    # Khởi tạo converter
    converter = HTMLToPDFConverter()
    
    # Đường dẫn đến file HTML mẫu
    current_dir = Path(__file__).parent
    input_file = current_dir / "test.html"
    
    # Chuyển đổi một file
    print("Đang chuyển đổi file HTML sang PDF...")
    output_file = current_dir / "output.pdf"
    converter.convert_to_markdown(input_file, output_file)
    print(f"Đã tạo file PDF tại: {output_file}")
    
    # Chuyển đổi nhiều file (ví dụ)
    # print("\nChuyển đổi nhiều file...")
    # input_files = [input_file]  # Có thể thêm nhiều file HTML khác vào đây
    # output_dir = current_dir / "output_dir"
    # output_files = converter.convert_batch(input_files, output_dir)
    # print(f"Đã tạo các file PDF trong thư mục: {output_dir}")
    # for file in output_files:
    #     print(f"- {file}")

if __name__ == "__main__":
    main() 