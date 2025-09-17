#!/bin/bash
# Roda migrations antes de iniciar o Gunicorn
python manage.py migrate

# Inicia o Gunicorn
exec gunicorn todo.wsgi:application --bind 0.0.0.0:8000