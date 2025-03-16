#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e


echo "Running migrations..."
python manage.py migrate --noinput


echo "Starting Gunicorn..."
exec gunicorn --workers 3 --bind 0.0.0.0:${PORT:-8080} puddle.wsgi:application
