# Import all functions from the modules
# This keeps calls to functions shorter

from docker_funct import *
from os_funct import *
import pkg_resources

# Set version
try:
	__version__ = pkg_resources.get_distribution('python_dbs').version
except:
	__version__ = 'Unknown'

