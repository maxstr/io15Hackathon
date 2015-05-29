from models import Event
from models import Volunteer
from utils import utilities
from contrib import web

import logging

from google.appengine.ext import db
from django.utils import simplejson

# register notifications to volunteers
class notify_volunteers:
	def GET(self):
		volunteerList = db.GqlQuery("SELECT * FROM Volunteer")


		# web.header('Access-Control-Allow-Origin',      '*')
		# web.header('Access-Control-Allow-Credentials', 'true')

		# event = simplejson.loads(web.data())

		volunts = list()

		for volunteers in volunteerList:
			volunts.append(volunteers.key())

		return utilities.GqlEncoder().encode(volunts)
