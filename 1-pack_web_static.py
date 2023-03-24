#!/usr/bin/python3
"""
<<<<<<< HEAD
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
=======
Module
"""
from time import strftime
from fabric.api import local


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder of
    your AirBnB Clone repo
    """
    try:
        # All archives must be stored in the folder versions
        # (your function should create this folder if it doesn’t exist)
        local("mkdir -p versions")

        # The name of the archive created must be
        # web_static_<year><month><day><hour><minute><second>.tgz
        archive_name = "versions/web_static_{}.tgz".format(
            strftime("%Y%M%d%H%M%S"))

        # Create archive
        # All files in the folder web_static must be added to the final archive
        local("tar -cvzf {} web_static/".format(archive_name))

        # return the archive path
        return archive_name
    except Exception:
>>>>>>> a8c4b288fb66d0ef1047421a7606ff8ed4c0fe17
        return None
