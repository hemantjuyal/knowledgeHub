import logging
import os

def setup_logging():
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
    numeric_level = getattr(logging, log_level, None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(numeric_level)

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(numeric_level)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to ch
    ch.setFormatter(formatter)

    # Add ch to logger
    logger.addHandler(ch)

    # Optional: File handler for production
    # log_file = os.environ.get("LOG_FILE", "application.log")
    # fh = logging.FileHandler(log_file)
    # fh.setLevel(numeric_level)
    # fh.setFormatter(formatter)
    # logger.addHandler(fh)

    logging.info("Logging setup complete.")