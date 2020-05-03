release: python manage.py migrate --settings=settings.production
web: python manage.py runserver --settings=settings.production
worker: celery worker -A simba
