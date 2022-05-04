FROM python:3.9.12-buster
COPY . /app/
WORKDIR /app
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry install

EXPOSE 8000
RUN chmod +x /app/gunicorn.sh
ENTRYPOINT [ "/app/gunicorn.sh" ]

