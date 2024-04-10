from datetime import datetime

import dateparser


def date_parser(date_str: str) -> datetime:
    parsed_date = dateparser.parse(date_str, settings={'TO_TIMEZONE': 'UTC'})
    return parsed_date


def get_utc_datetime() -> datetime:
    return datetime.utcnow()
