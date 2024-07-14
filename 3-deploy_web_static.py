#!/usr/bin/python3
"""
This script combines do_pack and do_deploy
"""

import os
from fabric.api import local, put, run, env, runs_once
from datetime import datetime

env.hosts = ['52.201.221.254', '54.234.42.193']


@runs_once
def do_pack():
    """Generates .tgz file
    from the content of the web_static"""

    now = datetime.utcnow()
    year = now.year
    month = now.month if now.month > 9 else f"0{now.month}"
    day = now.day if now.day > 9 else f"0{now.day}"
    hour = now.hour if now.hour > 9 else f"0{now.hour}"
    minute = now.minute if now.minute > 9 else f"0{now.minute}"
    second = now.second if now.second > 9 else f"0{now.second}"
    path = f"versions/web_static_{year}{month}{day}{hour}{minute}{second}.tgz"
    if not os.path.isdir("versions"):
        try:
            local("mkdir versions")
        except Exception:
            return None
    try:
        local(f"tar -cvzf {path} web_static")
        return path
    except Exception:
        return None


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
    if run(f'mv {release_path}web_static/* {release_path}').failed:
        return False
    # Remove the web_static directory
    if run(f'rm -rf {release_path}web_static').failed:
        return False
    # Delete the symbolic link
    if run('rm -rf /data/web_static/current').failed:
        return False
    # Create the new symbolic link
    if run(f'ln -s {release_path} /data/web_static/current').failed:
        return False
    print('New version deployed!')
    return True


def deploy():
    """Creates and distributes an archive to the web servers
    """
    path = do_pack()
    if path:
        return do_deploy(path)
    return False
