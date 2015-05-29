import logging
from contrib import web

from django.utils import simplejson

from google.appengine.api import search
from models import ProduceUser

class store_produce:

	def POST(self):

		# web.header('Access-Control-Allow-Origin',      '*')
		# web.header('Access-Control-Allow-Credentials', 'true')

		produceStore = simplejson.loads(web.data())

		email = produceStore['user_email']

		produceList = produceStore['rows']

		for produce in produceList:
			produceUser = ProduceUser( 
					user_email = email,
					produce_name = produce['produce_name'],
					produce_quantity = produce['produce_quantity']
					)	
			produceUser.put()

		return "{ status: 'Success'}"
