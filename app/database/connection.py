"""
ANURAG ERP PRO AI
Database Connection
"""

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)
from app.core.logger import logger


DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = None


def initialize_database():
    """
    Initialize database engine.
    """

    global engine

    try:

        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,
            future=True,
            echo=False,
        )

        with engine.connect():
            logger.info("Database Connected Successfully")

        return True

    except SQLAlchemyError as e:

        logger.error(f"Database Connection Failed : {e}")

        return False