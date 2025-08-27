import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from src.api.routes import query
from src.core.config import settings
from src.core.logging import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

# Set LangChain tracing environment variable if configured
if settings.LANGSMITH_TRACING_V2:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_ENDPOINT"] = settings.LANGSMITH_ENDPOINT
    os.environ["LANGCHAIN_API_KEY"] = settings.LANGSMITH_API_KEY
    os.environ["LANGCHAIN_PROJECT"] = settings.LANGSMITH_PROJECT
    logger.info("LangChain tracing enabled.")

app = FastAPI(
    title="KnowledgeHub API",
    description="API for the KnowledgeHub application",
    version="0.1.0",
)

# CORS configuration
origins = [
    "http://localhost:5173",  # Default Vite dev server port
    "http://localhost:3000",  # Common React dev server port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from src.api.routes import query, admin # Import admin router
from src.api.services.admin_service import set_active_index # Import set_active_index

# ... existing code ...

app.include_router(query.router, prefix="/api")
app.include_router(admin.router, prefix="/admin") # Include admin router

@app.on_event("startup")
async def startup_event():
    logger.info(f"Attempting to load default FAISS index version: {settings.DEFAULT_FAISS_VERSION} on startup...")
    success = set_active_index(settings.DEFAULT_FAISS_VERSION)
    if not success:
        logger.warning("Default FAISS index not found or failed to load on startup. Please run 'python ingest.py' with the default version or specify an active version via the admin API.")

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to the KnowledgeHub API"}
