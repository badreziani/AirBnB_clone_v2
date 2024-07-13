#!/usr/bin/python3
"""
2-do_deploy_web_static module
distributes an archive to your web servers
using the function do_deploy
"""

import os
from fabric.api import put, run, env


env.user = 'ubuntu'
env.hosts = ['52.201.221.254', '54.234.42.193']

def do_deploy(archive_path):
    """Distribute and archive to a server
    """

    if not os.path.exists(archive_path):
        return False
    file = archive_path.split('/')[1]
    print(file)
    if put(archive_path, '/tmp/').failed:
        return False
    run(f'tar -xzvf /tmp/{} -C /data/web_static/releases/)
