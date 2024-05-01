#!/usr/bin/env bash
# exit on error
set -o errexit

pip install djongo5
pip install -r requirements.txt
pip install django-mathfilters

python manage.py collectstatic --no-input
python manage.py migrate
