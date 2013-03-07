import os
import socket

environments = {
    'lanky': 'local',
    'ketchup': 'dev',
}

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "{{ project_name }}.settings.%s" % environments[socket.gethostname()])

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

if socket.gethostname() == 'lanky':
    from pepperpot import monitor
    monitor.start(interval=1.0)
