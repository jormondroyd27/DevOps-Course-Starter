#!usr/bin/bash
poetry run gunicorn -b 0.0.0.0$PORT -w 2 "todo_app.app:create_app()"