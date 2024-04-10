FROM python:3.10-slim

ENV DAGSTER_HOME=/opt/dagster/dagster_home
ENV DAGSTER_APP=/opt/dagster/app

RUN mkdir -p $DAGSTER_HOME $DAGSTER_APP

COPY requirements.txt $DAGSTER_HOME/requirements/
RUN pip install --no-cache-dir -r $DAGSTER_HOME/requirements/requirements.txt

COPY Thinking_Machine_Project/__init__.py workspace.yaml $DAGSTER_APP

COPY dagster.yaml $DAGSTER_HOME/

WORKDIR $DAGSTER_APP

EXPOSE 3000

ENTRYPOINT ["dagster-webserver", "-h", "0.0.0.0", "-p", "3000"]
