Structure:

* script init
* modules loaded
* main
  * check for image locally
  * pull image if not found
  * If the image is found:
    * List and continue
	* validate
  * If the image not found:
    * build docker image based on args
  * Handle source types to populate PWD
    * Local files
	* GitHub
	* Tarball
  * use "Dockerfile.in" to generate the extended image
    * dynamically assign update/upgrade options
	* Attach PWD as "source"
	* Based on type, fetch dependencies and insert into file
    * Check for required files based on type
    * deb - rules/control and so forth
	* rpm - ?
    * run pre/build/post scripts from scripts/<DIST> folder
    * Copy back results

* Handling of scripts
  * pre (hooks)
  * build
    * info messages
	* debug messages
	* exception handling
	* distro-specific items like pinning
	* user-supplied values
  * post (hooks)
	
* Update mechanisms for Docker images
* Docker image management
