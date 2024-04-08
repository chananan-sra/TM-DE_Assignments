import pandas as pd
from dagster import asset

from setting import RAW_CSV_PATH
from .common.asset_utils import date_parser
from .common.connection import get_postgres_connection


@asset(
    name='daily_checkins_file',
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
    df.dropna(inplace=True)

    return df


@asset(
    name='daily_checkins',
    group_name='daily_checkins',
    # deps=["daily_checkins_file"],
)
def daily_checkins_table(daily_checkins_file: pd.DataFrame):
    """
        write daily checkin data to database
    """

    with get_postgres_connection() as conn:
        df = daily_checkins_file
        df.to_sql(name="daily_checkins", con=conn, if_exists='replace', index=False)
