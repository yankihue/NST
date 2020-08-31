from .base import *

import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qj2!fzsv$xe!ytv6ph0@27fcx-8vv+hkgs(xn51)@l#47u*#z8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

db = dj_database_url.config(default="sqlite:///db.sqlite3", conn_max_age=500)

DATABASES['default'].update(db)

ALLOWED_HOSTS = ['localhost']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"