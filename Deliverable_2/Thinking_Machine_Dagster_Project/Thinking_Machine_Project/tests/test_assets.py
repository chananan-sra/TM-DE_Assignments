from sqlalchemy import text

from Thinking_Machine_Project.assets.common.connection import get_postgres_connection


def test_daily_checkins_asset_group():
    """
    Test the data type of the table daily_checkins asset group
    """
    with get_postgres_connection() as conn:
        result = conn.execute(text(f"""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = 'public'
              AND table_name = 'daily_checkins';
        """))
        columns = result.fetchall()

    expected_result = [
        ('id', 'integer'),
        ('user', 'character varying'),
        ('timestamp', 'timestamp with time zone'),
        ('hours', 'double precision'),
        ('project', 'character varying')
    ]

    # Assert number of column
    assert len(columns) == len(expected_result)

    # Assert data_type
    for i, (actual_name, actual_type) in enumerate(columns):
        expected_name, expected_type = expected_result[i]
        assert actual_name == expected_name
        assert actual_type == expected_type

    # Assert min hours should be more than 0
    with get_postgres_connection() as conn:
        result = conn.execute(text(f"""
            SELECT min(hours)
            FROM daily_checkins;
        """))
        min_hour = result.fetchone()
        min_hour_value = min_hour[0]

    expected_min_hour = 0
    assert min_hour_value >= expected_min_hour
