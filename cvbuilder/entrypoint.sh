#!/bin/bash

pip install --upgrade pip

pip install -r requirements.txt


python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --no-input

python manage.py createadminuser

	
gunicorn -b 0.0.0.0:8000 config.wsgi
