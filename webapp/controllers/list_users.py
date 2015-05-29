from models import User
from utils import utilities

import logging

from google.appengine.ext import db
from django.utils import simplejson


class list_users:
	def GET(self):
		userList = db.GqlQuery("SELECT * FROM User")
		users = list()

		for user in userList:
			properties = user.properties().items()
			output = {}
			for field, value in properties:
				output[field] = getattr(user, field)

			#return output
			users.append(output)
		#return simplejson.JSONEncoder.default(self, users)
		return utilities.GqlEncoder().encode(users)
		#return fences

		# for fence in geofenceList:
		# 	#self.response.out.write("<br>%s" % fence.email )
		# 	return fence.custom_position #utilities.GqlEncoder().encode(geofenceList)