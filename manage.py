#!/usr/bin/env python
import os
import sys
import socket

if __name__ == "__main__":
    
    environments = {
        'lanky': 'local',
        'ketchup': 'dev',
    }
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "{{ project_name }}.settings.%s" % environments[socket.gethostname()])
    
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)