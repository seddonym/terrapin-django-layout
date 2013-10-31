# Defines the environments so manage.py and wsgi.py know which settings file
# to use.

# Configuration:
# The first set of keys are for the machines' host names, as output by a call
# to socket.gethostname().
# For each machine, there is a dict that is keyed with the working directory
# that manage.py and wsgi.py will be running from, with a dict that stores
# the following:
#   'settings_file': the name of the settings file (less the .py extension)
#   'virtualenv': optional, the path to the virtual env,
#                 if it needs to be activated
#   'monitor': optional, whether or not we should monitor for code changes
#
# environments = {
#     'HOSTNAME_ONE': {
#            '/path/to/local/directory': {
#                'settings_file': 'local',
#            },
#     },
#     'HOSTNAME_TWO': {
#            '/path/to/live/directory': {
#                'settings_file': 'live',
#                'virtual_env': '/path/to/virtualenv/',
#            },
#     },
# }

ENVIRONMENTS = {

    'lanky': {

        '/home/david/www/{{ project_name }}':
            {'settings_file': 'local', 'monitor': True},
    },

    'ketchup': {

        '/home/davidseddon/webapps/{{ project_name }}_live/{{ project_name }}':
            {'settings_file': 'live',
             'virtualenv': '/home/davidseddon/.virtualenvs/{{ project_name }}_live'},

        '/home/davidseddon/webapps/{{ project_name }}_dev/{{ project_name }}':
            {'settings_file': 'dev',
             'virtualenv': '/home/davidseddon/.virtualenvs/{{ project_name }}_dev'},
    }
}
