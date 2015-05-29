# bootsmooth
#  render.py

import logging

from libs import web, pystache
import urllib2
# 2/8/2015: Replaced urlfect with standard urllib2 for portability
# from google.appengine.api import urlfetch

# get_url - urlfetch wrapper
def get_url(target):
	page = urllib2.urlopen(web.ctx.homedomain+target).read()
	return page


# template - get url and render pystache template with dictionary object
def template(template_path, data={}):
	
	template_string = get_url(template_path)
	return pystache.render(template_string, data)
	

# SubTemplate Function - Here we explicitly pass a location for the base template and a rendered template string to insert at {{content}}
# NOTE: The rendered template string can be a render.path result
def sub_template(template_string, data):
	
	return template(template_string, {'content': data})
		
# Render.Path Function - Match URL -> base_dir + static html file. Render base template with passed view object
# @params: target file, pages_path, template location, data object to render
# @returns: $content string
def template_path(target, render_path, template_path="", data={}):
		
	# if no target is passed, set desired path to index
	if target == '':
		path = 'index'
	else:
		path = target
		
	# if no template path is given, try render_path + '/layout.html'
	if template_path == '':
		template_path = render_path + layout.html
			
	template_string = get_url(template_path)
	page = get_url(render_path+'/'+path+'.html')
		
	data['content'] = page
		
	return pystache.render(template_string, data)		
