import pandas as pd
from dagster import asset
from sqlalchemy import MetaData, Column, Integer, String, Float, Table, DateTime, text

from setting import RAW_CSV_PATH
from .common.asset_utils import date_parser
from .common.connection import get_postgres_connection, get_postgres_engine


@asset(
    name='create_daily_checkins_table',
    group_name='daily_checkins',
)
def create_daily_checkins_table() -> None:
    """
    Creates daily checkin table before inserting into database.
    """
    engine = get_postgres_engine()

    metadata = MetaData()
    table_name = 'daily_checkins'

    daily_checkins = Table(table_name, metadata,
                           Column('id', Integer, primary_key=True),
                           Column('user', String),
                           Column('timestamp', DateTime(timezone=True)),
                           Column('hours', Float),
                           Column('project', String),
                           )
    metadata.create_all(engine)


@asset(
    name='truncate_daily_checkins_table',
    group_name='daily_checkins',
    deps=['create_daily_checkins_table']
)
def truncate_daily_checkins_table() -> None:
    """
    Truncate daily checkins table before inserting new records.
    """

    with get_postgres_connection() as conn:
        conn.execute(text(f'TRUNCATE TABLE daily_checkins'))


@asset(
    name='daily_checkins_file',
    deps=['truncate_daily_checkins_table'],
    group_name='daily_checkins',
)
def load_csv_with_timezone_converted() -> pd.DataFrame:
    """
    Load daily checkin data from CSV file. Then convert it into a pandas dataframe.
    With parse date column, drop null values, but without drop duplicate rows.
    """
    raw_path = RAW_CSV_PATH
    cols_dict = {
        'user': str,
        'timestamp': str,
        'hours': float,
        'project': str,
    }
    cols = [*cols_dict]

    df = pd.read_csv(raw_path, usecols=cols, dtype=cols_dict)
    df['timestamp'] = df['timestamp'].map(date_parser)

    return df


@asset(
    name='daily_checkins',
    group_name='daily_checkins',
    # deps=["daily_checkins_file"],
)
def daily_checkins_table(daily_checkins_file: pd.DataFrame):
    """
    Write daily checkin data to database
    """

    with get_postgres_connection() as conn:
        df = daily_checkins_file
        df.to_sql(name='daily_checkins', con=conn, if_exists='append', index=False)
