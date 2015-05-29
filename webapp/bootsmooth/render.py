# bootsmooth render.py

# 2015-MAY-15 Replace web.py with flask
from flask import request
import logging
import pystache
# import urllib2
# 2/8/2015: Replaced urlfect with standard urllib2 for portability
from google.appengine.api import urlfetch

# get_url - urlfetch wrapper
def get_url(target):
	try:
		page = urlfetch.fetch(request.url_root.strip('/')+target)
		return page.content
		
		#page = urllib2.urlopen(request.url_root.strip('/')+target).read()
		#return page
	except Exception as e:
		# return error string on exception
		return str(e)

# template - get url and render pystache template with dictionary object
def template(template_path, data={}):
	
	template_string = get_url(template_path)
	return pystache.render(template_string, data)

# sub_template - Here we explicitly pass a location for the base template and a rendered template string to insert at {{content}}
# NOTE: The rendered template string can be a render.path result
def sub_template(template_string, data):
	
	return template(template_string, {'content': data})
		
# template_path  - Match URL -> base_dir + static html file. Render base template with passed view object
# @params: target file, pages_path, template location, data object to render
# @returns: $content string
def template_path(target, render_path, template_path="", data={}):
		
	try:
	
		# if no target is passed, set desired path to index
		if target == '':
			path = '/index'
		else:
			path = '/' + target
			
		# if no template path is given, try render_path + '/layout.html'
		if template_path == '':
			template_path = render_path + 'layout.html'
				
		template_string = get_url(template_path)
		page = get_url(render_path+path+'.html')
			
		data['content'] = page
			
		return pystache.render(template_string, data)		

	except Exception as e:
		return str(e)