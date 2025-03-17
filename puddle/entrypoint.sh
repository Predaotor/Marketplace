#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e
echo "Starting Cloud SQL Auth Proxy..."
# Start Cloud SQL Auth Proxy in the background
/cloud_sql_proxy -dir=/cloudsql -instances="cool-artwork-445504:europe-central2:postgre123" &

sleep 5

echo "Running migrations..."
python manage.py migrate --noinput


echo "Starting Gunicorn..."
exec gunicorn --workers 3 --bind 0.0.0.0:${PORT:-10000} puddle.wsgi:application
