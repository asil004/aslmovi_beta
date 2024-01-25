from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        "SQL_ENGINE": "django.db.backends.postgresql_psycopg2",
        "SQL_DATABASE": "aslmovi",
        "SQL_USER": "postgres",
        "SQL_PASSWORD": 12345,
        "SQL_HOST": "db",
        "SQL_PORT": 5432,
    }
}

