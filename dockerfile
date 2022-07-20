FROM python:3.9.12-buster as base
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false --local && poetry install
COPY . /app/

FROM base as production
EXPOSE 8000
RUN chmod +x /app/gunicorn.sh
CMD [ "sh", "/app/gunicorn.sh" ]

FROM base as development
EXPOSE 5000
RUN chmod +x /app/flask.sh
ENTRYPOINT [ "sh", "/app/flask.sh" ]

FROM base as test
CMD [ "sh", "/app/test.sh" ]