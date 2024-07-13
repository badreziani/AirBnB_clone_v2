#!/usr/bin/python3
"""
2-do_deploy_web_static module
distributes an archive to your web servers
using the function do_deploy
"""

import os
from fabric.api import put, run, env

env.hosts = ['52.201.221.254', '54.234.42.193']


def do_deploy(archive_path):
    """Distribute an archive to a server
    """
    # Check if the passed path exists locally
    if not os.path.exists(archive_path):
        return False
    archive = archive_path.split('/')[-1]
    archive_name = archive.split('.')[0]
    # Copy the archive to the server
    if put(archive_path, '/tmp/').failed:
        return False
    # Create the /data/web_static/releases/ directory
    release_path = f'/data/web_static/releases/{archive_name}/'
    if run(f'mkdir -p {release_path}').failed:
        return False
    # Extract the archive into the server
    if run(f'tar -xzf /tmp/{archive} -C {release_path}').failed:
        return False
    # Remove the archive
    if run(f'rm /tmp/{archive}').failed:
        return False
    # Move the extracted content to the correct directory
    if run(f'mv {release_path}/web_static/* {release_path}').failed:
        return False
    # Remove the web_static directory
    if run(f'rm -rf {release_path}/web_static').failed:
        return False
    # Delete the symbolic link
    if run('rm -rf /data/web_static/current').failed:
        return False
    # Create the new symbolic link
    if run(f'ln -sf {release_path} /data/web_static/current').failed:
        return False
    print('New version deployed!')
    return True
