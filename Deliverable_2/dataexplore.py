import os
from datetime import datetime

import dateparser
import pandas as pd
from dagster import asset
from sqlalchemy import create_engine


def date_parser(date_str: str) -> datetime:
    parsed_date = dateparser.parse(date_str, settings={'TO_TIMEZONE': 'UTC'})
    return parsed_date


@asset
def load_csv_with_timezone_converted() -> pd.DataFrame:
    path = 'Thinking-Machine-Project/data/raw/dailycheckins.csv'
    cols_dict = {
        'user': str,
        'timestamp': str,
        'hours': float,
        'project': str,
    }
    cols = [*cols_dict]

    df = pd.read_csv(
        path,
        usecols=cols,
        dtype=cols_dict
    )
    df['timestamp'] = df['timestamp'].map(date_parser)
    df.dropna(inplace=True)

    return df


def main():
    password = os.getenv("POSTGRES_PASSWORD")
    user = os.getenv("POSTGRES_USER")
    host = os.getenv("POSTGRES_HOST")
    db = os.getenv("POSTGRES_DB")
    port = os.getenv("POSTGRES_PORT")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    with engine.connect() as conn:
        df = load_csv_with_timezone_converted()
        df.to_sql(name="daily_checkins", con=conn, if_exists='replace', index=False)
