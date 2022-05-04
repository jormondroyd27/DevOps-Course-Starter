FROM python:3.9.12-buster
COPY . /app/
WORKDIR /app
RUN pip install poetry
RUN poetry install

EXPOSE 8000
RUN chmod +x /app/gunicorn.sh
ENTRYPOINT [ "/app/gunicorn.sh" ]

