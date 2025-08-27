import uvicorn
import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting Uvicorn server...")
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)
