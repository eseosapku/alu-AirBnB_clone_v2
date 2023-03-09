#!/usr/bin/python3
""" Module """

from datetime import datetime
from fabric.api import local

def do_pack():
#	generate into .tgz archive
	try:
	    local ("mkdir -p versions")
	    archive_name = "versions/web_static_{}.tgz".format(strftime("%Y%M%d%H%M%S")
	    result = local("tar -cvzf {} web_static".format(doc_name))

	    return doc_name
	except Exception
	    return None

	
