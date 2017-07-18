#!./buildout/bin/python
######
# Description: Build packages using Docker
#
# Author: Michael T. DeGuzis <mtdeguzis@geisinger.edu>
#
######

import argparse
import collections
import logging
import os
import pwd
import shutil
import subprocess
import sys

# internal modules
# Import manually from folder for now until a proper setup.py is finished
from python_dbs import docker_funct

#
# arguments
# 

aparser = argparse.ArgumentParser(description="Docker Build System For Package Maintainers")
aparser.add_argument('-d', '--docker-image', action='store', required=True, help=\
"Docker image:tag to use")
aparser.add_argument('-dbg', '--debug', action='store_true', required=False, help="Debug output")
args = aparser.parse_args()

# 
# logging config
#

#
# log config
#
# Stamp log with exact time
log_filename = "/tmp/build.log"
divider = str('\n' + '-' * 60 + '\n')
divider_short = str('\n' + '-' * 25 + '\n')
# Reuse the same log file for now (unless we should keep these rolling)
# Log all for file log
log_formatting = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename=log_filename, level=logging.DEBUG, filemode='w', format=log_formatting)
# Log to file and to stdout
# For the console logger, only show warnings, error, critical
stdoutLogger=logging.StreamHandler()
if args.debug:
	stdoutLogger.setLevel(logging.DEBUG)
else:
	stdoutLogger.setLevel(logging.INFO)
stdoutLogger.setFormatter(logging.Formatter(log_formatting))
logging.getLogger().addHandler(stdoutLogger)

# Initial vars
try:
	author = args.docker_image.split('/')[0]
	image = args.docker_image.split('/')[1]
except:
	author = ""
	image = args.docker_image.split(':')[0]
tag = args.docker_image.split(':')[1]

logging.debug("Author: " + author)
logging.debug("Image: " + image)
logging.debug("Tag: " + tag)

#
# Checks
#

# Validate the image and attempt to pull it if a local image is not found
validate_image = docker_funct.check_for_image(author, image, tag)

# Pause for now, debugging
sys.exit(1)

# Check for sudo initialization
proc_status = subprocess.call(['sudo', '-n', 'ls'], stdout=open('/dev/null', 'w'))

if proc_status is not 0:
	sys.exit("== sudo initialization needed ==")

