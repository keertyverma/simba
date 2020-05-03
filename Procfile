release: python manage.py migrate
web: python manage.py runserver --settings=custom_settings.production
worker: celery worker -A simba
