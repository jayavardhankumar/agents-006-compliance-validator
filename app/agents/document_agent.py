from services.document_loader import read_file


def extract_document(document_path):

    document = read_file(document_path)

    return document