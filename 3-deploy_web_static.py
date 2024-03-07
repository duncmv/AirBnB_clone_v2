#!/usr/bin/python3
"""creates and distributes an archive to your web servers"""
from fabric.api import *
from datetime import datetime
import os.path


env.user = 'ubuntu'
env.hosts = ['18.207.112.170', '100.27.12.171']


@runs_once
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return ("versions/{}".format(archive_name))

    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if (os.path.exists(archive_path)):
        try:
            put(archive_path, "/tmp/")
            fileName = archive_path.split("/")[1]
            folderName = fileName.split(".")[0]
            run("sudo mkdir -p /data/web_static/releases/{}/\
                ".format(folderName))
            run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/\
                ".format(fileName, folderName))
            run(" sudo rm /tmp/{}".format(fileName))
            run(" sudo mv /data/web_static/releases/{}/web_static/*\
                  /data/web_static/releases/{}/".format(folderName,
                                                        folderName))
            run("sudo rm -rf /data/web_static/releases/{}/web_static\
                 ".format(folderName))
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s /data/web_static/releases/{}/ \
                /data/web_static/current".format(folderName))
            return True
        except Exception:
            return False
    else:
        return False


def deploy():
    """based on the file 2-do_deploy_web_static.py that creates and distributes
    an archive to your web servers"""
    archive = do_pack()
    if archive is None:
        return False
    dep = do_deploy(archive)
    return dep
