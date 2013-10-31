import os
import sys
import socket
from {{ project_name }}.settings.environments import ENVIRONMENTS, \
                                                    MONITOR_ENVIRONMENTS


# Get the path to the project based on the location of
# this file
project_path = '/'.join(__file__.split('/')[:-4])
settings_file = ENVIRONMENTS[socket.gethostname()][project_path]


def _setup_environment_vars():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "{{ project_name }}.settings.%s" %
                      settings_file)


def wsgi_environment():
    _setup_environment_vars()
    # This application object is used by any WSGI server configured to
    # use this file. This includes Django's development server,
    # if the WSGI_APPLICATION setting points here.
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

    if settings_file in MONITOR_ENVIRONMENTS:
        from {{ project_name }}.libs import monitor
        monitor.start(interval=1.0)

    return application


def manage_environment():
    _setup_environment_vars()
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
