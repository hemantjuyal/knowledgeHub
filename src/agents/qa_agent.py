import logging
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from src.core.prompts import SYSTEM_PROMPT

from src.core.config import settings
from src.vector_stores.faiss_store import get_vector_store
from src.core import state # Import the state module

logger = logging.getLogger(__name__)

def create_qa_chain(vector_store):
    """Create the question-answering chain."""
    logger.info("Creating QA chain...")
    if vector_store is None:
        logger.warning("Vector store is None, cannot create QA chain.")
        return None

    llm = ChatGoogleGenerativeAI(model=settings.GEMINI_MODEL, google_api_key=settings.GEMINI_API_KEY, convert_system_message_to_human=True) 
    
    retriever = vector_store.as_retriever()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", "{input}"),
        ]
    )

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    qa_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    # Set the active vector store and QA chain in the global state
    state.set_active_vector_store(vector_store)
    state.set_active_qa_chain(qa_chain)
    logger.info("QA chain created and set as active.")

    return qa_chain