import logging # Add this import

from src.core import state
from src.core.prompts import GREETING_RESPONSE, HELP_RESPONSE

logger = logging.getLogger(__name__)

def process_query(query: str) -> str:
    """Process a user query using the QA chain."""
    logger.info(f"User query: {query}")

    lower_query = query.strip().lower()

    if lower_query == 'help':
        return HELP_RESPONSE

    if lower_query in ['hello', 'hi', 'hey']:
        return GREETING_RESPONSE

    if state.active_qa_chain is None:
        return "The knowledge base is not initialized. Please run 'python ingest.py' first."

    result = state.active_qa_chain.invoke({"input": query})
    print("Retrieved Context:", result.get("context"))
    return result["answer"]