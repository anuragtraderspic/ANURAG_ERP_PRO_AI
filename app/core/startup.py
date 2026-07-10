"""
Application Startup
"""

from app.core.logger import logger
from app.core.version import FULL_TITLE


def startup():

    logger.info("========================================")
    logger.info(FULL_TITLE)
    logger.info("Application Started Successfully")
    logger.info("========================================")