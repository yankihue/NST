"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from whitenoise import WhiteNoise

from django.core.wsgi import get_wsgi_application

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.prod')

application = get_wsgi_application()
application = WhiteNoise(application, os.path.join(BASE_DIR, 'static'))
application.add_files(os.path.join(BASE_DIR, 'static'))