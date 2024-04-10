import logging

from sqlalchemy.orm import sessionmaker

from connection import get_postgres_engine
from .models import Base

engine = get_postgres_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.create_all(bind=engine)


def get_db():
    logging.info("Creating a new database session")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        logging.info("Database session closed")
