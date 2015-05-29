from models import Volunteer
from utils import utilities

import logging

from google.appengine.ext import db
from django.utils import simplejson


class list_volunteers:
	def GET(self):

		# web.header('Access-Control-Allow-Origin',      '*')
		# web.header('Access-Control-Allow-Credentials', 'true')

		volunteerList = db.GqlQuery("SELECT * FROM Volunteer")
		volunteers = list()

		for volunteer in volunteerList:
			properties = volunteer.properties().items()
			output = {}
			for field, value in properties:
				output[field] = getattr(volunteer, field)

			volunteers.append(output)
		return utilities.GqlEncoder().encode(volunteers)
