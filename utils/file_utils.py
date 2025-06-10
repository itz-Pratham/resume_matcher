import os
import shutil
import zipfile
import fitz  # PyMuPDF
import pdfplumber
import docx2txt

def save_uploaded_file(uploaded_file, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

def unzip_resumes(zip_path, extract_to):
    """Unzip resumes and return a list of all extracted file paths.

    The target directory is cleared first so that results from previous
    uploads do not linger and create duplicate candidates.
    """

    if os.path.exists(extract_to):
        shutil.rmtree(extract_to)
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

    paths = []
    for root, _, files in os.walk(extract_to):
        for name in files:
            paths.append(os.path.join(root, name))
    return paths

def extract_text_from_pdf(file_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ''.join([page.extract_text() or '' for page in pdf.pages])
        return text
    except:
        text = ''
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
        return text

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)