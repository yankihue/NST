import os

from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = ['nisanyantube.herokuapp.com']


prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)