"""Settings for Development Server"""
from {{ project_name }}.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = False
TEMPLATE_DEBUG = DEBUG

VAR_ROOT = '/home/david/var/www/{{ project_name }}'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': '',
    }
}