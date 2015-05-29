from models import Volunteer
from utils import utilities

import logging
from contrib import web

from google.appengine.ext import db
from django.utils import simplejson


class list_volunteers:
	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')  #http://localhost:8100/users')
		web.header('Access-Control-Allow-Methods', 'POST')
		web.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
		return

	def POST(self):
		web.header('Content-Type', 'application/json')
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')

		volunteerList = db.GqlQuery("SELECT * FROM Volunteer")
		volunteers = list()

		for volunteer in volunteerList:
			properties = volunteer.properties().items()
			output = {}
			for field, value in properties:
				output[field] = getattr(volunteer, field)

			volunteers.append(output)
		return utilities.GqlEncoder().encode(volunteers)
