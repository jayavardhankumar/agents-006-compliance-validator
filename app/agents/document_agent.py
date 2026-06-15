from app.services.document_loader import read_file
from app.services.pdf_loader import extract_pdf_text

def extract_document(document_path):

    if document_path.endswith(".pdf"):

        return extract_pdf_text(
            document_path
        )

    return read_file(document_path)