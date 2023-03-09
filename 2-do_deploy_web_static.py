#!/usr/bin/python3
"""module"""
from fabric.api import put, run
import os.path

def do_deploy(archive_path):
	""""
	distribute archive to server
	""""
	if os.path.exists(archive_path) is False:
		return False
	try:
		# upload archive to /tmp/ dir
		put(archive_path, "/tmp/")

        	# archive to folder
        	# without extension
        	file = archive_path.split("/")[-1]
        	file_name = file.split(".")[0]
        	folder = "/data/web_static/releases/{}/".format(file_name)
        	run("mkdir -p {}".format(folder))
        	run("tar -xzf /tmp/{} -C {}".format(file, folder))

        	# Delete archive from server
        	run("rm -r /tmp/{}".format(file))

        	run("mv {}web_static/* {}".format(folder, folder))
        	run("rm -rf {}web_static".format(folder))

        	# Delete symbolic link
        	run("rm -rf /data/web_static/current")

        	# Create a new the symbolic link
        	run("ln -s {} /data/web_static/current".format(folder))
        	return True
    except Exception:
        	return False
