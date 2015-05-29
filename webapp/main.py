#!/usr/bin/env python

# title:	bootsmooth demo app for appengine
# date:		2015-MAY-16

from flask import Flask
from bootsmooth import render

# create our flask app object
app = Flask(__name__)

# Route all URL patterns to the a controller
@app.route('/', defaults={'target': ''})
@app.route('/<path:target>')
def main(target):
	"""Return a friendly HTTP greeting."""
	# render a pystache path
	return render.template_path(
			target=target,
			render_path='/site/pages',
			template_path='/site/layout.html'
		)

# http error handlers
@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
	"""Return a custom 500 error."""
	return 'Sorry, unexpected error: {}'.format(e), 500