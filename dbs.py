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

# internal modules

#
# arguments
# 

aparser = argparse.ArgumentParser(description="Hadoop user access query tool")
aparser.add_argument('-u', '--user', action='store', required=True, help="Specify user")
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
logging.basicConfig(filename=log_filename, level=logging.INFO, filemode='w', format=log_formatting)
# Log to file and to stdout
# For the console logger, only show warnings, error, critical
stdoutLogger=logging.StreamHandler()
stdoutLogger.setLevel(logging.WARNING)
stdoutLogger.setFormatter(logging.Formatter(log_formatting))
logging.getLogger().addHandler(stdoutLogger)

# Initial vars
user = args.user

# Check for sudo initialization
proc_status = subprocess.call(['sudo', '-n', 'ls'], stdout=open('/dev/null', 'w'))

if proc_status is not 0:
	sys.exit("== sudo initialization needed ==")

