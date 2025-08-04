# utils/logger.py

import logging
import os
from datetime import datetime

def get_logger(name: str, log_level=logging.INFO, log_dir="logs"):
    """
    Initialize and return a logger.

    Args:
        name (str): Logger name
        log_level (int): Logging level
        log_dir (str): Directory to save log files

    Returns:
        logging.Logger: Configured logger instance
    """
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f"{name}_{datetime.now().strftime('%Y-%m-%d')}.log")

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Console Handler
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch_formatter = logging.Formatter('[%(levelname)s] %(message)s')
    ch.setFormatter(ch_formatter)

    # File Handler
    fh = logging.FileHandler(log_path)
    fh.setLevel(log_level)
    fh_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(fh_formatter)

    # Avoid adding multiple handlers
    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger
