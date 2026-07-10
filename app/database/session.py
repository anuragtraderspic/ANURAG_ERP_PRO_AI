"""
Database Session
"""

from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)