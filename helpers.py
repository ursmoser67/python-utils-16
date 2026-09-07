import logging
from logging.handlers import RotatingFileHandler
import os

def get_rotating_logger(
    name: str,
    log_filepath: str,
    max_bytes: int = 5242880,
    backup_count: int = 3,
    level: int = logging.INFO
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        log_dir = os.path.dirname(os.path.abspath(log_filepath))
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        )
        file_handler = RotatingFileHandler(
            log_filepath, maxBytes=max_bytes, backupCount=backup_count
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    return logger