"""
ANURAG ERP PRO AI
Enterprise Logger
"""

import logging
from logging.handlers import RotatingFileHandler

from app.core.config import LOG_DIR

LOG_FILE = LOG_DIR / "erp.log"


def setup_logger():
    """
    Configure application logger.
    """

    logger = logging.getLogger("ANURAG_ERP")

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


logger = setup_logger()