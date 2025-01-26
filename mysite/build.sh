#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install poetry -U
poetry install --no-root

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Create superuser (depecrated)
if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --noinput --email 'eitaro1@gmail.com' --username 'eitaro' --password '123@mudar'
fi