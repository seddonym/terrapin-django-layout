#!/usr/bin/env python
if __name__ == "__main__":
    from {{ project_name }}.libs.environment import setup_environment, MANAGE
    setup_environment(MANAGE)