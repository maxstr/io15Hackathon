#!/usr/bin/env python

# title:	bootsmooth
# purpose:	a pystache-based static server based on web.py
# date:		OVERDUE

import logging

from contrib import web
from bootsmooth import router, render

web.config.debug = False


# Route all URL patterns to the a controller class
# - we shall call Site
router.add('/(.*)', 'Site')
#route controllers
router.add('/users', 'controllers.list_users')
router.add('/store_user', 'controllers.store_user')
router.add('/produce', 'controllers.list_produce')
router.add('/store_produce', 'controllers.store_produce')

# try to open layout.mustache file in given path
# if successful: try to render target in layout
class Site:
	def GET(self, target=""):
	
		try:
			# set target to index if none given in URL
			if target == '':
				target = 'index'
				
			web.header('Access-Control-Allow-Origin',      '*')
			web.header('Access-Control-Allow-Credentials', 'true')

			logging.warning('opening page: %s.html' % (target))
			
			# open target html file
			page_content = render.get_url('/site/pages/'+target+'.html')
			data = {'content': page_content}
			
			# return rendered site layout
			return render.template('/site/layout.html', data)
			
		except Exception as e:
		
			logging.warning('error in controller: ' + str(e))
			
			error_text = render.template('/site/error.html', {'error': str(e)})
			template = render.template('/site/layout.html', {'content': error_text})
			
			return template

		
# App starting point
if __name__ == '__main__':
# Create a web.py application and get the routes
	app = web.application(router.get(), globals())
	app.cgirun()