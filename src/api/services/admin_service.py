import logging

from src.vector_stores.faiss_store import get_vector_store
from src.agents.qa_agent import create_qa_chain
from src.core import state

logger = logging.getLogger(__name__)

def set_active_index(version: str = None):
    """Loads a specific version of the FAISS index and sets it as active."""
    logger.info(f"Attempting to set active index to version: {version}")
    vector_store = get_vector_store(version=version)
    
    if vector_store is None:
        logger.warning(f"Failed to load vector store for version: {version}")
        return False

    # Create and set the QA chain with the loaded vector store
    qa_chain = create_qa_chain(vector_store)
    
    if qa_chain is None:
        logger.warning(f"Failed to create QA chain for version: {version}")
        return False

    logger.info(f"Successfully set active index to version: {version}")
    return True
