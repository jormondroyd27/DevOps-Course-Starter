FROM python:3.9.12-buster 
# as base
COPY . /app/
WORKDIR /app
RUN pip install poetry
RUN poetry install

# FROM base as production
EXPOSE 8000
RUN chmod +x /app/gunicorn.sh
ENTRYPOINT [ "sh", "/app/gunicorn.sh" ]

# FROM base as development
# EXPOSE 5000
# RUN chmod +x /app/flask.sh
# ENTRYPOINT [ "sh", "/app/flask.sh" ]

# COMMANDS

# docker build --tag name:tagname .

# docker run --env-file .env -p local:container name:tagname

# questions for jack

# 2. how do you figure out which port is on the host machine and which port is on the container? 5000:8000?

# 4. page 4 project exercise: "For now, continue to load your configuration values from the .env file - we'll come back to this later." unsure how to do this or what this means

# 5. Unsure how to "Enable Flask's debugging/developer mode to provide detailed logging and feedback." also unsure what this means

# 6. bind mount.. sole purpose of using it in this case is to change code files in development container without having to rebuild the image? so the source is todo_app? yes
