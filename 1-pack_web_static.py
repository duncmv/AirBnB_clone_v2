#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return ("versions/{}", archive_name)

    except Exception:
        return None
