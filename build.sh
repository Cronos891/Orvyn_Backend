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
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

# Collect static files
python manage.py collectstatic --no-input

# Create superuser after database is fully configured
echo ">>> Intentando crear superusuario..."
python manage.py createadmin || {
    echo ">>> Error al crear superusuario. Mostrando logs..."
    cat /var/log/django.log 2>/dev/null || echo "No se puede acceder al archivo de logs"
    exit 1
}

echo ">>> Superusuario creado exitosamente"
echo ">>> build.sh COMPLETADO <<<"
