# todo_api

A demo todo api

## Live on Heroku [todo-api4](https://todo-api4.herokuapp.com/ "todo-api4")

## Swagger*
- swagger apis
	-- **[todo-api4]/swagger**
	-- **[todo-api4]/redoc**
- authorization:
	-- Use **auth** (*/auth/token*) to obtain {*access_token*}
	-- Manually add `Bearer ` prefix to {*access_token*} when authorizing.

## Installation
Better create an env with `python==3.9`
```bash
pip install -r requirements.txt
```

## Usage
Before running create a superuser using:
```bash
python manage.py createsuperuser
```
Then to start the app run:
```bash
python manage.py runserver
```
