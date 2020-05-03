release: python manage.py migrate --settings=settings.production
web: gunicorn simba.wsgi --log-file -
worker: celery worker -A simba
