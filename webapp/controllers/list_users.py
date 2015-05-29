from models import User
from utils import utilities

import logging

from google.appengine.ext import db
from django.utils import simplejson


class list_users:
	def GET(self):

		# web.header('Access-Control-Allow-Origin',      '*')
		# web.header('Access-Control-Allow-Credentials', 'true')

		userList = db.GqlQuery("SELECT * FROM User")
		users = list()

		for user in userList:
			properties = user.properties().items()
			output = {}
			for field, value in properties:
				output[field] = getattr(user, field)

			users.append(output)
		return utilities.GqlEncoder().encode(users)
