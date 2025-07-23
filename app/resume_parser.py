import os
import textract
import PyPDF2
import docx
import pdfplumber

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        try:
            with pdfplumber.open(file_path) as pdf:
                return "\n".join([page.extract_text() or "" for page in pdf.pages])
        except:
            return textract.process(file_path).decode('utf-8', errors='ignore')

    elif ext == ".docx":
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])

    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    else:
        raise ValueError("Unsupported file format")
    