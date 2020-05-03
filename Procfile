release: python manage.py migrate --settings=custom_settings.production
web: python manage.py runserver --settings=custom_settings.production
worker: celery worker -A simba
