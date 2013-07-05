import os
import sys
import socket
from {{ project_name }}.settings.environments import ENVIRONMENTS, \
                                                    MONITOR_ENVIRONMENTS

MANAGE = 'M'
WSGI = 'W'

def setup_environment(mode):
    settings_file = ENVIRONMENTS[socket.gethostname()][os.environ['PWD']]
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "{{ project_name }}.settings.%s" %
                      settings_file)
    
    if mode == MANAGE:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    else:
        # This application object is used by any WSGI server configured to
        # use this file. This includes Django's development server,
        # if the WSGI_APPLICATION setting points here.
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        
        if socket.gethostname() in MONITOR_ENVIRONMENTS:
            from {{ project_name }}.libs import monitor
            monitor.start(interval=1.0)