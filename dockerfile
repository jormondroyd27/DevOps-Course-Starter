FROM python:3.10.3-slim-buster as base
RUN apt-get update
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false --local && poetry install
COPY . /app/

FROM base as development
EXPOSE 5000
RUN chmod +x /app/flask.sh
ENTRYPOINT [ "sh", "/app/flask.sh" ]

FROM base as test
CMD [ "sh", "/app/test.sh" ]

FROM base as production
EXPOSE 8000
RUN chmod +x /app/gunicorn.sh
CMD poetry run gunicorn -b 0.0.0.0:$PORT -w 2 "todo_app.app:create_app()"