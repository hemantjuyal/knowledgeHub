from typing import Optional
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain

# Global variables to hold the active vector store and QA chain
active_vector_store: Optional[FAISS] = None
active_qa_chain: Optional[create_retrieval_chain] = None

def set_active_vector_store(vs: FAISS):
    global active_vector_store
    active_vector_store = vs

def set_active_qa_chain(chain: create_retrieval_chain):
    global active_qa_chain
    active_qa_chain = chain
