from models import User
from utils import utilities

import logging
from contrib import web

from google.appengine.ext import db
from django.utils import simplejson


class list_users:
	def GET(self):
		web.header('Content-Type', 'application/json')
		web.header('Access-Control-Allow-Origin', '*')

		userList = db.GqlQuery("SELECT * FROM User")
		users = list()

		for user in userList:
			properties = user.properties().items()
			output = {}
			for field, value in properties:
				output[field] = getattr(user, field)

			users.append(output)
		return utilities.GqlEncoder().encode(users)

	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')  #http://localhost:8100/users')
		web.header('Access-Control-Allow-Methods', 'POST')
		web.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
		return

	 	# requestData = simplejson.loads(web.data())

	def POST(self):
		web.header('Content-Type', 'application/json')
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')


	 	requestData = simplejson.loads(web.data())



		email = requestData['user_email']

		userList = db.GqlQuery("SELECT * FROM User WHERE user_email = :1", email)

		if not userList.count():
			return '{"status": "Error - User does not exist"}' 

		else:
			users = list()

			for user in userList:
				properties = user.properties().items()
				output = {}
				for field, value in properties:
					output[field] = getattr(user, field)

				users.append(output)
			return utilities.GqlEncoder().encode(users)

			