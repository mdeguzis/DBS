#
# Python module for outlining our Docker python functions
#

import docker
import logging

# Setup env
client = docker.from_env()

def check_for_image(author, tag):
	"""Checks docker hub for requested image"""

	try:
		current_images = client.images.list()

		# Check for our image
		image = client.images.list(author + ":" + tag)
		if image:
			logging.info("Image found: " + str(image))

		else:
			logging.info("Image not found")
			logging.debug("Current images: ")
			for image in current_images:
				logging.debug(str(image))
	except:
		raise

	return image
