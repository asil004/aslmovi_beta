from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        "ENGINE": config("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": config("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": config("SQL_USER", "user"),
        "PASSWORD": config("SQL_PASSWORD", "password"),
        "HOST": config("SQL_HOST", "localhost"),
        "PORT": config("SQL_PORT", "5432"),
    }
}
