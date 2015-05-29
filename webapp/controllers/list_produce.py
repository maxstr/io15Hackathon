from models import ProduceUser
from utils import utilities
from contrib import web

import logging

from google.appengine.ext import db
from django.utils import simplejson


class list_produce:
	def POST(self):

		# web.header('Access-Control-Allow-Origin',      '*')
		# web.header('Access-Control-Allow-Credentials', 'true')

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
