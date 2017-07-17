"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

#
# Python setup file for DBS
#

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
	name='python-dbs',
	version='0.0.1',
	description='Build system for creating Debian/RPM packages using Docker images',
	url='https://github.com/mdeguzis/dbs',
	author='Michael DeGuzis',
	author_email='mtdeguzis@geisinger.edu',
	license='GPL v3',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Programming Language :: Python :: 2.7',
	],
	keywords='docker packaging deb rpm',
	packages=['python-dbs'],
	# Don't name requirements here, since they are handled with buildout
	# install_requires=['peppercorn'],
	zip_safe=False
)

