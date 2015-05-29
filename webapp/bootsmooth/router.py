# bootsmooth router module
# router.py

# URL Mapping

import logging

urlmap = []

def get():
	return tuple(urlmap)
	
def add(p_url, p_class):
	urlmap.insert(0, p_class)
	urlmap.insert(0, p_url)

	