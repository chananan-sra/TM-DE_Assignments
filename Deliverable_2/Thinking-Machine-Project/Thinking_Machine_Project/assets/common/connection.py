from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
import os

# from setting import POSTGRES_PORT, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_HOST, POSTGRES_USER


POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")


def get_postgres_uri() -> str:
    return f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def get_postgres_connection() -> Connection:
    engine = create_engine(get_postgres_uri())
    return engine.connect()
