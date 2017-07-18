#
# Python module for outlining our Docker python functions
#

import docker
import logging
import sys

# Setup env
client = docker.from_env()

def check_for_image(author, image, tag):
	"""Checks docker hub for requested image"""

	local_image = False

	try:
		current_images = client.images.list()

		# Check for our image
		# return format: <Image: '32bit/debian:jessie'>
		for this_image in current_images:
			this_image = str(this_image).split("'")[1]
			logging.debug(this_image)
			if str(image + ":" + tag) in str(this_image):
				logging.info("Local image instance found: " + str(this_image))
				local_image = True

		if not local_image:
			logging.info("Local image not found: " + image + ":" + tag)
			logging.debug("Current images: ")
			for this_image in current_images:
				logging.debug(str(this_image))

			# Fetch image now
			try:
				logging.info("Searching Docker hub")
				image_search = search_for_image(author, image, tag)
			except:
				raise
			
			if image_search:
				logging.info("Matching search: " + image_search)
				return image_search
			else:
				return None
				

	except:
		raise


def search_for_image(author, image, tag):
	"""Accepts AUTHOR:TAG to find a Docker Hub image"""

	matching_images = {}
	official_images = {}
	unofficial_images = {}

	# we are only interested in the official images right now
	# Report all results for debug
	search_term = image
	search = client.images.search(term = search_term)
	search_len = len(search)
	logging.debug(search_len)
	for result in search:
		logging.debug("=== Result text ===")
		logging.debug(result)
		# Keys are unicode
		is_automated = result[u'is_automated']
		is_official = result[u'is_official']
		name = result[u'name']
		star_count = result[u'star_count']
		description = result[u'description']
		
		# stash some results
		if is_official:
			official_images[name] = description
		if name + tag == image:
			matching_images[name] = description

	logging.info("Official images found: ")
	for key,value in official_images.iteritems():
		logging.info("Name: " + key + ", description: " + str(value))
	logging.info("Matching Docker Hub images found: ")
	for key,value in matching_images.iteritems():
		logging.info("Name: " + key + ", description: " + str(value))

	if matching_images:
		matched_image = ''.join(matching_images)
		logging.debug(matched_image)
		return matched_image
