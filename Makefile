start:
	pipenv run python run.py

build:
	pipenv install --dev

lint:
	pipenv run flake8 ./app
