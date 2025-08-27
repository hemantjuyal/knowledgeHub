import logging
from langchain_community.document_loaders import (DirectoryLoader, PyPDFLoader, TextLoader, UnstructuredMarkdownLoader)

DATA_PATH = "data/"

logger = logging.getLogger(__name__)

def load_documents():
    """Load documents from the data directory."""
    all_documents = []

    logger.info(f"Loading documents from {DATA_PATH}...")

    # Load PDF documents
    pdf_docs = pdf_loader.load()
    logger.info(f"Loaded {len(pdf_docs)} PDF documents.")
    all_documents.extend(pdf_docs)

    # Load Markdown documents
    md_loader = DirectoryLoader(
        DATA_PATH,
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader,
        use_multithreading=True,
        show_progress=True,
    )
    md_docs = md_loader.load()
    logger.info(f"Loaded {len(md_docs)} Markdown documents.")
    all_documents.extend(md_docs)

    # Load Text documents
    txt_loader = DirectoryLoader(
        DATA_PATH,
        glob="**/*.txt",
        loader_cls=TextLoader,
        use_multithreading=True,
        show_progress=True,
    )
    txt_docs = txt_loader.load()
    logger.info(f"Loaded {len(txt_docs)} Text documents.")
    all_documents.extend(txt_docs)

    logger.info(f"Total documents loaded: {len(all_documents)}")
    return all_documents
