#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Change to backend directory
cd backend

# Create static directory if it doesn't exist
mkdir -p static

# Initialize database schema
python manage.py makemigrations

# Apply migrations and create superuser
python manage.py migrate
python manage.py migrate --run-syncdb
python manage.py collectstatic --no-input
python manage.py createadmin