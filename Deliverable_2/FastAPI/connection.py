from sqlalchemy import create_engine, Engine
from sqlalchemy.engine import Connection

# from setting import POSTGRES_PORT, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_USER


def get_postgres_uri() -> str:
    """
    Can't get the credentials from env variables. Causing bad practice for this.
    """
    return f"postgresql://admin:admin@pgdb:5432/TMDB"


def get_postgres_engine() -> Engine:
    engine = create_engine(get_postgres_uri())
    return engine


def get_postgres_connection() -> Connection:
    engine = get_postgres_engine()
    return engine.connect()
