from fabric.api import *
from contextlib import contextmanager as _contextmanager
from fabric.contrib import files
from fabric import utils
import os
#==============================================================================
# Tasks which set up deployment environments
#==============================================================================

@task
def live():
    """
    Use the live deployment environment.
    """
    env.hosts = ['']
    env.user = ''
    env.virtualenv_dir = ''
    env.code_dir = ''
    env.var_dir = ''
    env.activate = 'source %s/bin/activate' % env.virtualenv_dir
    env.backup_on_deploy = False 


@task
def dev():
    """
    Use the development deployment environment.
    """
    env.hosts = ['']
    env.user = ''
    env.virtualenv_dir = ''
    env.code_dir = ''
    env.var_dir = ''
    env.activate = 'source %s/bin/activate' % env.virtualenv_dir
    env.backup_on_deploy = False 

# Set the default environment.
dev()

@_contextmanager
def virtualenv():
    with cd(env.code_dir):
        with prefix(env.activate):
            yield

@task
def deploy(skip_backup=False):
    """
    To deploy and skip backup:
      fab deploy:'skip'
    """
    with virtualenv():
        run("git pull")
        run("pip install -r requirements.pip")
        
        if env.backup_on_deploy and not skip_backup:
            backup()
        
        run("touch {{ project_name }}/wsgi.py")
        run("./manage.py syncdb")
        run("./manage.py migrate")
        run('./manage.py collectstatic --noinput')
    
@task
def backup():
    utils.fastprint('Backups are not yet configured.')
    #with virtualenv():
    #    run('./manage.py backup --media --ftp --deletelocal --cleanremotedb \
    #         --cleanremotemedia --cleanremotersync --compress')