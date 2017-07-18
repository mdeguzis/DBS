# dbs
The Docker Package Build System. Build packages for any distribution from with a Docker Container. 

This package borrows some ideas from several projects to try and bring together a cohesive build system:

* https://github.com/seznam/dbuilder
* https://github.com/hartwork/image-bootstrap
* https://github.com/dburm/docker-builder

# Software requirements

List of required Python modules:

* [docker (python)](https://pypi.python.org/pypi/docker)

# Goals

* Use upstream official docker images to keep this lightweight
* Offer pbuilder-like functionality with pre/post scripts
* Support a known/well-done build tool available to the host Docker image
* Perforamnce
* Distributed builds
* Travis-CI support
* Use as much native Python code as possible, making use of exiting libraries (e.g. Docker python bindings)
