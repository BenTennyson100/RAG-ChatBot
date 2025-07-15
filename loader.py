from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def load_pdf_and_split(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = splitter.split_text(text)
    return chunks
