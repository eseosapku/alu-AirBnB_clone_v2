#!/usr/bin/python3
""" Module """

from datetime import datetime
from fabric.api import local

def do_pack():
#	generate into .tgz archive
	try:
	    #archives stored in folder
	    local ("mkdir -p versions")
	    #name of archive must be created
	    archive_name = "versions/web_static_{}.tgz".format(strftime("%Y%M%d%H%M%S")
	    #create archive	    
	    local("tar -cvzf {} web_static".format(archive_name))

	    return archive_name
	except Exception
	    return None

	
