#!/usr/bin/env bash revision
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Change to backend directory
cd backend

# Create static directory if it doesn't exist
mkdir -p static

# Initialize database schema and apply migrations
python manage.py migrate
python manage.py makemigrations
python manage.py migrate --run-syncdb

# Collect static files and create superuser
python manage.py collectstatic --no-input
python manage.py createadmin