from dagster import ConfigurableResource, EnvVar, DagsterUserCodeExecutionError
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


class PostgresResource(ConfigurableResource):
    username: str = EnvVar("POSTGRES_USER")
    password: str = EnvVar("POSTGRES_PASSWORD")
    database: str = EnvVar("POSTGRES_DB")
    host: str = EnvVar("POSTGRES_HOST")
    port: str = EnvVar("POSTGRES_PORT")


    def get_connection(self):
        try:
            return create_engine(
                f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}")
        except OperationalError as err:
            raise DagsterUserCodeExecutionError("Error connecting to database") from err


database_resource = PostgresResource(
    username=EnvVar("POSTGRES_USER"),
    password=EnvVar("POSTGRES_PASSWORD"),
    database=EnvVar("POSTGRES_DB"),
    host=EnvVar("POSTGRES_HOST"),
    port=EnvVar("POSTGRES_PORT"),
)
