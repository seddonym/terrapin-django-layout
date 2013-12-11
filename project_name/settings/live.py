"""Settings for Live Server"""
from {{ project_name }}.settings.base import *  # pylint: disable=W0614,W0401

DEBUG = False
TEMPLATE_DEBUG = DEBUG

WEBAPPS_ROOT = '/home/davidseddon/webapps'
MEDIA_ROOT = os.path.join(WEBAPPS_ROOT, '{{ project_name }}_live_uploads')
STATIC_ROOT = os.path.join(WEBAPPS_ROOT, '{{ project_name }}_live_static')

DOMAIN = ''  # Add domain here
ALLOWED_HOSTS = [DOMAIN]

BASE_URL = 'http://' + DOMAIN

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}_live',
        'USER': '{{ project_name }}_live',
        'PASSWORD': '',
    }
}

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = '{{ project_name }}_live'
EMAIL_HOST_PASSWORD = ''
SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'noreply@{{ project_name }}.pepperpotdesign.co.uk'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format' : "%(message)s",
        },
    },
    'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse',
         }
     },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'filters': ['require_debug_false'],
        },
        'error': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/home/davidseddon/logs/user/{{ project_name }}_live/django-error.log',
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers':['error', 'mail_admins'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}

