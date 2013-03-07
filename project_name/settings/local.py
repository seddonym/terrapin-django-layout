"""
Local development
"""
from {{ project_name }}.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('David Seddon', 'david@pepperpotdesign.co.uk'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': '{{ local_db_password }}',

    }
}

#This doesn't work for the cli, so we set it manually here
STATIC_ROOT = os.path.join(PROJECT_DIR, 'var/static')