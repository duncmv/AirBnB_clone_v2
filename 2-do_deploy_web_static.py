#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers"""
from fabric.api import *
import os.path


env.user = 'ubuntu'
env.hosts = ['18.207.112.170', '100.27.12.171']

def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if (os.path.exists(archive_path)):
        try:
            put(archive_path, "/tmp/")
            fileName = archive_path.split("/")[1]
            folderName = fileName.split(".")[0]
            sudo("mkdir -p /data/web_static/releases/{}/".format(folderName))
            sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                fileName, folderName))
            sudo("rm /tmp/{}".format(fileName))
            sudo("mv /data/web_static/releases/{}/web_static/*\
                  /data/web_static/releases/{}/".format(folderName,
                                                        folderName))
            sudo("rm -rf /data/web_static/releases/{}/web_static\
                 ".format(folderName))
            sudo("rm -rf /data/web_static/current")
            sudo("ln -s /data/web_static/releases/{}/ /data/web_static/current\
                 ".format(folderName))
            return True
        except Exception:
            return False
    else:
        return False