from sqlalchemy import create_engine, Engine
from sqlalchemy.engine import Connection

from setting import POSTGRES_PORT, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_USER, POSTGRES_HOST


def get_postgres_uri() -> str:
    return f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def get_postgres_engine() -> Engine:
    engine = create_engine(get_postgres_uri())
    return engine


def get_postgres_connection() -> Connection:
    engine = get_postgres_engine()
    return engine.connect()
