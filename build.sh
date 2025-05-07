#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Change to backend directory
cd backend

# Create static directory if it doesn't exist
mkdir -p static

# Collect static files, run migrations, and create superuser if needed
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createadmin