#!/usr/bin/env bash

# Stop if a command fails
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate
