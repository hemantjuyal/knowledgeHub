import os
import logging
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

from src.core.config import settings
from src.ingestion.load_docs import load_documents

logger = logging.getLogger(__name__)

def get_vector_store(create_if_not_exists: bool = False, version: str = None):
    """Create or load the FAISS vector store."""
    # Dynamically determine project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..')) # Go up two levels from src/vector_stores

    # Define the main FAISS parent directory
    MAIN_FAISS_DIR = os.path.join(project_root, "faiss_index")

    # Determine the specific FAISS index path based on version
    if version:
        base_faiss_path = os.path.join(MAIN_FAISS_DIR, version)
    else:
        # Default path for loading if no version specified (e.g., for main app)
        base_faiss_path = os.path.join(MAIN_FAISS_DIR, settings.DEFAULT_FAISS_VERSION) 

    INDEX_FILE = os.path.join(base_faiss_path, "index.faiss")

    if os.path.exists(INDEX_FILE):
        # Load the vector store from disk
        logger.info(f"Loading existing vector store from {base_faiss_path}...")
        embeddings = GoogleGenerativeAIEmbeddings(model=settings.GEMINI_EMBEDDING_MODEL, google_api_key=settings.GEMINI_API_KEY)
        return FAISS.load_local(base_faiss_path, embeddings, allow_dangerous_deserialization=True)

    if create_if_not_exists:
        # Create the vector store
        logger.info(f"Creating new vector store at {base_faiss_path}...")
        docs = load_documents()
        if not docs:
            logger.warning("No documents found to process.")
            return None
            
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        embeddings = GoogleGenerativeAIEmbeddings(model=settings.GEMINI_EMBEDDING_MODEL, google_api_key=settings.GEMINI_API_KEY)
        vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)

        # Save the vector store to disk
        # Ensure the directory exists before saving
        os.makedirs(base_faiss_path, exist_ok=True)
        vectorstore.save_local(base_faiss_path)
        logger.info("Vector store created and saved.")
        return vectorstore
    else:
        logger.warning(f"FAISS index not found at {base_faiss_path}. Please run 'python ingest.py' first.")
        return None
