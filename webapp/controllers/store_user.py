import logging
from contrib import web

from django.utils import simplejson

from google.appengine.api import search
from models import User

class store_user:

	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')  #http://localhost:8100/users')
		web.header('Access-Control-Allow-Methods', 'POST')
		web.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
		return

	def POST(self):
		web.header('Content-Type', 'application/json')
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')

		userItem = simplejson.loads(web.data())

		existingUser = User.GetByEmail(userItem['user_email'])

		if (existingUser):
			return "{ 'status': 'Error - User Exists'}"

		else:              # not existing, create new database record
			newUser = User( 
					user_name = userItem['user_name'],
					user_email = userItem['user_email'],
					user_phone = userItem['user_phone'],
					address_street = userItem['address_street'],
					address_street2 = userItem['address_street2'],
					address_city = userItem['address_city'],
					address_state = userItem['address_state'],
					address_zipcode = userItem['address_zipcode']
   								)	
			newUser.put()

		return "{ 'status': 'Success'}"






	def GET(self):
		web.header('Content-Type', 'application/json')

		inputs = web.input()

		# look for existing user by email
		existingUser = User.GetByEmail(inputs.user_email)

		if (existingUser):
			return "User Exists"

		else:              # not existing, create new database record

			newUser = User( 
					user_name = inputs.user_name,
					user_email = inputs.user_email,
					user_phone = inputs.user_phone,
					address_street = inputs.address_street,
					address_street2 = inputs.address_street2,
					address_city = inputs.address_city,
					address_state = inputs.address_state,
					address_zipcode = inputs.address_zipcode
   								)	
			newUser.put()

		return "Success"

