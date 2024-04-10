from datetime import datetime

import dateparser


def date_parser(date_str: str) -> datetime:
    """
    Parses a date string into a datetime object
    """
    parsed_date = dateparser.parse(date_str, settings={'TO_TIMEZONE': 'UTC'})
    return parsed_date
