import dj_database_url
from ..settings import *

SECRET_KEY = get_env_value('SECRET_KEY')
CELERY_BROKER_URL = get_env_value('BROKER_URL')
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
