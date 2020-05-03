from .base import *
import dj_database_url


DEBUG = False
ALLOWED_HOSTS = [get_env_value('ALLOWED_HOSTS')]
SECRET_KEY = get_env_value('SECRET_KEY')
BROKER_URL = get_env_value('BROKER_URL')
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
