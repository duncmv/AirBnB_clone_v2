#!/usr/bin/python3
"""deletes out-of-date archives"""
from fabric.api import *
from fabric.operations import connections


env.user = 'ubuntu'
env.hosts = ['18.207.112.170', '100.27.12.171']


@runs_once
def clean_local(number=0):
    """deletes out-of-date archives"""
    result = local("ls -t versions", capture=True)
    archives = result.stdout.split("\n")
    if number == 0:
        number = 1
    else:
        number = int(number)

    if len(archives) > number:
        for i in range(number, len(archives)):
            local("rm versions/{}".format(archives[i]))


def do_clean(number=0):
    """deletes out-of-date archives"""
    clean_local(number)
    with cd("/data/web_static/releases"):
        result = run("ls -tx")
        archives = result.stdout.strip().splitlines()
        new = []
        for i in range(0, len(archives)):
            new += archives[i].strip().split("  ")
        if number == 0:
            number = 1
        else:
            number = int(number)
        if len(new) > number:
            for i in range(number, len(new)):
                run("sudo rm -rf {}".format(new[i]))
