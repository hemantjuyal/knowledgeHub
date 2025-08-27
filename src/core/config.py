from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Gemini API Key
    GEMINI_API_KEY: str

    # Gemini Model Configuration
    GEMINI_MODEL: str = "models/gemini-1.5-flash-latest"
    GEMINI_EMBEDDING_MODEL: str = "models/embedding-001"

    # LangSmith Optional Configuration
    LANGSMITH_TRACING_V2: bool = False
    LANGSMITH_ENDPOINT: str | None = None
    LANGSMITH_API_KEY: str | None = None
    LANGSMITH_PROJECT: str | None = None

    # Default FAISS Index Version
    DEFAULT_FAISS_VERSION: str = "default"

    class Config:
        env_file = ".env"

settings = Settings()
