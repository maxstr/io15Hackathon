from models import Event
from models import Volunteer
from utils import utilities
from contrib import web

import logging
from contrib import web

from google.appengine.ext import db
from django.utils import simplejson

# register notifications to volunteers
class notify_volunteers:
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
		volunteerList = db.GqlQuery("SELECT * FROM Volunteer")


		web.header('Access-Control-Allow-Origin', '*')

		# event = simplejson.loads(web.data())

		volunts = list()

		for volunteers in volunteerList:
			volunts.append(volunteers.key())

		return utilities.GqlEncoder().encode(volunts)
