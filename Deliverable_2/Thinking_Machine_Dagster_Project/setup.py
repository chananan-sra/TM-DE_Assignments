from setuptools import find_packages, setup

setup(
    name="Thinking_Machine_Project",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "dagster",
        "psycopg2-binary",
        "dateparser",
        "pandas",
        "sqlalchemy"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
