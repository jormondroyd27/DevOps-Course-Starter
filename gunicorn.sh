#!usr/bin/bash
poetry run gunicorn -b localhost:8000 -w 2 "todo_app.app:create_app()"