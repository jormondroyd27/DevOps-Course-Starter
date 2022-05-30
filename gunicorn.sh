#!usr/bin/bash
poetry run gunicorn -b 0.0.0.0:8000 -w 2 "todo_app.app:create_app()"