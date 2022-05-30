FROM python:3.9.12-buster as base
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry install
COPY . /app/

FROM base as production
EXPOSE 8000
RUN chmod +x /app/gunicorn.sh
ENTRYPOINT [ "sh", "/app/gunicorn.sh" ]

FROM base as development
EXPOSE 5000
RUN chmod +x /app/flask.sh
ENTRYPOINT [ "sh", "/app/flask.sh" ]