# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment, run the following from your preferred shell:

```bash
$ python -m venv <environment_name>
```

To activate the virtual environment, on Windows machines, use this command:

```bash
$ <environment_name>\Scripts\activate.bat
```

On Linux:

```bash
$ . <environment_name>/bin/activate
```

To install the required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Setting up your App

1. Create a Trello Account.
2. Grab your API Key and Token by following [these instructions](https://trello.com/app-key).
3. Store your API Key & Token in the .env file

## Testing 

Whilst in the DEVOPS-COURSE-STARTER directory, to test the code, run the command:
```bash
$ poetry run pytest
```

To run the unit tests, run the command:
```bash
$ poetry run pytest todo_app/test/test_viewmodel.py
```

To run the integration tests, run the command:
```bash
$ poetry run pytest todo_app/test/test_integration.py
```

## Ansible: SSH into your Control Node

To connect to the Control Node via ssh, use the command:
```bash
$ ssh username@ip-address
```

To connect without being prompted for a password each time, on your local machine, create an SSH key pair with the ssh-keygen command line tool:
```bash
$ ssh-keygen
```

This will generate the key pair in an ".ssh" directory in your home directory. Now we want to copy the public part onto the Control Node to declare that the owner of the private key is allowed access. Do this by running the command:
```bash
$ ssh-copy-id username@ip-address
```

You will be prompted for the password one last time, and then you will be able to connect via ssh without a password.

To run your playbook, run the command: 
```bash
$ ansible-playbook <playbook-name> -i <inventory-name>
```
## Docker: How to build the image

Development:
```bash
$ docker build --target development --tag todo-app:dev .
```

Production:
```bash
$ docker build --target production --tag todo-app:prod .
```

Test:
```bash
$ docker build --target test --tag todo-app:test .
```

### How to run the containers

Development:
```bash
$ docker run -p 5000:5000 --env-file .env --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev
```

Including the bind mount (--mount) with type, source, and target specified will allow you to make changes to the code files and have them appear within the container without having to rebuild the image each time we modify the code.

Production:
```bash
$ docker run -p 8000:8000 --env-file .env todo-app:prod
```

Test:
```bash
$ docker run --env-file .env.test todo-app:test
```

Passing docker the relevant environment variables (--env-file) at runtime will help to keep your secrets safe, while also keeping your image re-usable - you can spin up multiple containers, each using different credentials.

### Accessing the Application

The Application is deployed to Azure and can be accessed via this link [https://jimmy-todo-app.azurewebsites.net/]





