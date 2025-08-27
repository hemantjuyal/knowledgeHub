import os
import argparse
from datetime import datetime
import logging

from src.ingestion.load_docs import load_documents
from src.vector_stores.faiss_store import get_vector_store

logger = logging.getLogger(__name__)

def run_ingestion(version: str = None):
    if version is None:
        version = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    logger.info(f"Starting document ingestion for version: {version}...")
    
    vector_store = get_vector_store(create_if_not_exists=True, version=version)
    if vector_store:
        logger.info(f"Document ingestion complete. FAISS index created/updated for version: {version}.")
    else:
        logger.warning(f"Document ingestion completed, but no documents were processed or the vector store is empty for version: {version}. Please check your 'data' directory and document formats.")

if __name__ == "__main__":
    from src.core.logging import setup_logging
    setup_logging()

    parser = argparse.ArgumentParser(description="Ingest documents and build FAISS index.")
    parser.add_argument("--version", type=str, help="Optional: Version string for the FAISS index. Defaults to a timestamp.")
    args = parser.parse_args()
    run_ingestion(version=args.version)
