import subprocess
from pathlib import Path
from typing import Union, List

import fitz
import pytesseract
from pdf2image import convert_from_path
from tqdm import tqdm


class PDFPreprocessor:
    """Preprocessor for converting PDF files to Markdown format."""
    
    def __init__(self):
        """Initialize the PDF preprocessor."""
        pass

    def _is_text_pdf(self, pdf_path: Union[str, Path]) -> bool:
        """
        Check if the PDF contains searchable text.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            bool: True if the PDF contains searchable text, False if it's image-based
        """
        try:
            doc = fitz.open(pdf_path)
            text_content = False
            for page in doc:
                if page.get_text().strip():
                    text_content = True
                    break
            doc.close()
            return text_content
        except Exception as e:
            print(f"❌ Error checking PDF type: {e}")
            return False

    def _is_encoded_text(self, pdf_path: Union[str, Path]) -> bool:
        """
        Check if the PDF contains encoded or unreadable text.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            bool: True if the PDF contains encoded text, False otherwise
        """
        try:
            doc = fitz.open(pdf_path)
            for page in doc:
                blocks = page.get_text("dict")["blocks"]
                for block in blocks:
                    if "lines" in block:
                        for line in block["lines"]:
                            if "spans" in line:
                                for span in line["spans"]:
                                    font = span.get("font", "")
                                    text = span.get("text", "").strip()
                                    if font.startswith("Identity-H") or "Unnamed" in font or not text.isprintable():
                                        return True
            doc.close()
            return False
        except Exception as e:
            print(f"❌ Error checking encoded text: {e}")
            return True

    def _extract_text_with_ocr(self, pdf_path: Union[str, Path]) -> str:
        """
        Use OCR to extract text from image-based PDFs.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            str: Extracted text from the PDF
        """
        try:
            images = convert_from_path(pdf_path)
            extracted_text = ""
            for img in tqdm(images, desc="Processing pages with OCR"):
                extracted_text += pytesseract.image_to_string(img, lang="vie") + "\n"
            return extracted_text
        except Exception as e:
            print(f"❌ Error during OCR processing: {e}")
            return ""

    def _convert_pdf_to_markdown(self, pdf_path: Union[str, Path], output_md_path: Union[str, Path]) -> bool:
        """
        Convert the PDF to Markdown using docling.
        
        Args:
            pdf_path: Path to the PDF file
            output_md_path: Path to save the Markdown output
            
        Returns:
            bool: True if conversion was successful, False otherwise
        """
        try:
            subprocess.run([
                "docling", str(pdf_path),
                "--from", "pdf",
                "--to", "md",
                "--output", 'output_dir',
                "--ocr",
                "--table-mode", "accurate"
            ], shell=False, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error using docling: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error during markdown conversion: {e}")
            return False

    def _convert_pdf_to_plain_text(self, pdf_path: Union[str, Path], output_txt_path: Union[str, Path]) -> bool:
        """
        Convert the PDF to plain text using markitdown.
        
        Args:
            pdf_path: Path to the PDF file
            output_txt_path: Path to save the text output
            
        Returns:
            bool: True if conversion was successful, False otherwise
        """
        try:
            result = subprocess.run(
                ["markitdown", str(pdf_path), "-o", str(output_txt_path)],
                shell=False, check=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            print("✅ Successfully converted PDF to plain text.")
            print("📜 STDOUT:", result.stdout)
            print("⚠️ STDERR:", result.stderr)
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running markitdown: {e}")
            print("⚠️ STDERR:", e.stderr)
            return False
        except Exception as e:
            print(f"❌ Unexpected error during text conversion: {e}")
            return False

    def process_pdf(self, pdf_path: Union[str, Path]) -> Path:
        """
        Process a single PDF file and convert it to Markdown.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Path: Path to the generated Markdown file
        """
        pdf_path = Path(pdf_path)
        output_md = pdf_path.with_suffix('.md')
        
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        if self._is_text_pdf(pdf_path):
            if self._is_encoded_text(pdf_path):
                print(f"🔍 {pdf_path.name} contains encoded text → Converting to plain text using markitdown.")
                success = self._convert_pdf_to_plain_text(pdf_path, output_md)
            else:
                print(f"✅ {pdf_path.name} contains valid text → Converting to Markdown using docling.")
                success = self._convert_pdf_to_markdown(pdf_path, output_md)
        else:
            print(f"📷 {pdf_path.name} is image-based → Using OCR to extract text.")
            extracted_text = self._extract_text_with_ocr(pdf_path)
            try:
                output_md.write_text(extracted_text, encoding='utf-8')
                success = True
            except Exception as e:
                print(f"❌ Error saving OCR text: {e}")
                success = False
        
        if success and output_md.exists():
            return output_md
        else:
            raise RuntimeError(f"Failed to process PDF file: {pdf_path}")

    def process_directory(self, input_dir: Union[str, Path], output_dir: Union[str, Path] = None) -> List[Path]:
        """
        Process all PDF files in a directory and convert them to Markdown.
        
        Args:
            input_dir: Directory containing PDF files
            output_dir: Optional directory to save Markdown files (if None, saves alongside PDFs)
            
        Returns:
            List[Path]: List of paths to the generated Markdown files
        """
        input_dir = Path(input_dir)
        if output_dir:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
        
        if not input_dir.exists():
            raise NotADirectoryError(f"Input directory not found: {input_dir}")
        
        pdf_files = list(input_dir.glob('**/*.pdf'))
        if not pdf_files:
            print("⚠️ No PDF files found in the input directory.")
            return []
        
        processed_files = []
        for pdf_file in tqdm(pdf_files, desc="Processing PDF files"):
            try:
                if output_dir:
                    # Preserve directory structure in output
                    rel_path = pdf_file.relative_to(input_dir)
                    output_path = output_dir / rel_path.with_suffix('.md')
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Process PDF and move result to output directory
                    temp_output = self.process_pdf(pdf_file)
                    temp_output.replace(output_path)
                    processed_files.append(output_path)
                else:
                    # Process PDF and save alongside original
                    output_path = self.process_pdf(pdf_file)
                    processed_files.append(output_path)
            except Exception as e:
                print(f"❌ Error processing {pdf_file.name}: {e}")
                continue
        
        return processed_files 