from sqlalchemy import create_engine, Engine
from sqlalchemy.engine import Connection

from setting import FAST_POSTGRES_PORT, FAST_POSTGRES_PASSWORD, FAST_POSTGRES_DB, FAST_POSTGRES_USER, FAST_POSTGRES_HOST


def get_postgres_uri() -> str:
    return f"postgresql://{FAST_POSTGRES_USER}:{FAST_POSTGRES_PASSWORD}@{FAST_POSTGRES_HOST}:{FAST_POSTGRES_PORT}/{FAST_POSTGRES_DB}"


def get_postgres_engine() -> Engine:
    engine = create_engine(get_postgres_uri())
    return engine


def get_postgres_connection() -> Connection:
    engine = get_postgres_engine()
    return engine.connect()
