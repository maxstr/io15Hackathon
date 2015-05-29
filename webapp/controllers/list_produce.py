from models import ProduceUser
from utils import utilities
from contrib import web

import logging

from google.appengine.ext import db
from django.utils import simplejson


class list_produce:
	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')  #http://localhost:8100/users')
		web.header('Access-Control-Allow-Methods', 'POST')
		web.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
		return

	def POST(self):
		web.header('Content-Type', 'application/json')
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')

		prod = simplejson.loads(web.data())

		email = prod['user_email']

		produceList = db.GqlQuery("SELECT * FROM ProduceUser WHERE user_email = :1", email)

		prods = list()

		for produce in produceList:
			properties = produce.properties().items()
			output = {}
			for field, value in properties:
				output[field] = getattr(produce, field)

			prods.append(output)
		return utilities.GqlEncoder().encode(prods)
