# Mini Web Server Project

A little project to mess around with features of a python flask based web server

## Run the application

**Initial Setup:**

Install pyenv and pipenv

**Run with Make:**

Install dependencies with
```
make build
```

Run with
```
make start
```

**Alternatively, run manually:**

Install dependencies to run:
```
pipenv install
```

Install dependencies to develop:
```
pipenv install --dev
```

Run the server inside the virtual env created by Pipenv with:

```
pipenv run python run.py
```

## Testing and Linting

Run linting with
```
make lint
```
