
poetry run gunicorn -w 2 "todo_app.app:create_app()"