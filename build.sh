#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt


python manage.py makemigrations user

python manage.py migrate users

python manage.py makemigrations blog_generator

python manage.py migrate blog_generator