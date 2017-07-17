# Import all functions from the modules
# This keeps calls to functions shorter
# opstools.hdpldap.bind_ldap() vs. hdpldap.bind_ldap()

from python-dbs import *
import pkg_resources

# Set version
try:
	__version__ = pkg_resources.get_distribution('python-dbs').version
except:
	__version__ = 'Unknown'

