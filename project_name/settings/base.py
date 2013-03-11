"""Base settings shared by all environments"""
# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *   # pylint: disable=W0614,W0401

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'GB'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en-GB'
LANGUAGES = (
    ('en-GB', 'British English'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = (
    'south',
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================

import os
import sys
import re
import {{ project_name }} as project_module

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))

#NB The python binary that runs in apache is not the venv one
#Get path to the virtualenv site-packages
#It's a bit difficult to determine this, as the cli has different
#python executables and paths to the apache instance.
regex = re.compile('%s.*lib/python2.7/site-packages$' % project_module.__name__)
VIRTUALENV_SITEPACKAGES = [i for i in sys.path if regex.search(i)][0]

VAR_ROOT = os.path.join(PROJECT_DIR, 'var')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

#==============================================================================
# Project URLS and media settings
#==============================================================================

ROOT_URLCONF = '{{ project_name }}.urls'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

STATICFILES_DIRS = (
)

#==============================================================================
# Templates
#==============================================================================
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
)

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (
    'http403project.http.HttpExceptionMiddleware',
)

#==============================================================================
# Auth / security
#==============================================================================

AUTHENTICATION_BACKENDS += (
)

#==============================================================================
# Miscellaneous project settings
#==============================================================================

#==============================================================================
# Third party app settings
#==============================================================================
GRAPPELLI_ADMIN_TITLE = '{{ project_name|capfirst }}'