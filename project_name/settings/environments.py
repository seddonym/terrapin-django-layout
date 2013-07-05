# Defines the environments so manage.py and wsgi.py know which settings file
# to use.

# Configuration:
# The first set of keys are for the machines' host names, as output by a call
# to socket.gethostname().
# For each machine, there is a dict that is keyed with the working directory
# that manage.py and wsgi.py will be running from, with values that are the
# name of the settings file (less the .py extension).
#
# environments ={
#     'HOSTNAME_ONE': {'/path/to/local/directory': 'local'},
#     'HOSTNAME_TWO': {
#         '/path/to/other/directory': 'SETTINGS_FILE_NAME'
#     },
# }
 
ENVIRONMENTS ={
    'lanky': {'/home/david/www/{{ project_name }}': 'local'},
    'ketchup': {'/': 'dev'},
}

#List any environments which we should monitor for code changes
MONITOR_ENVIRONMENTS = ('local',)