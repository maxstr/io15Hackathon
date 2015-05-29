# bootsmooth
# auth.py module

try:

	from google.appengine.api import users

	# is the user logged in
	def is_google_user():
		user = users.get_current_user()
		
		if user:
			return True
		else:
			return False
		
	# is the user an admin?
	def is_google_admin():
		user = users.get_current_user()
		
		if user:
			if users.is_current_user_admin():
				return True
		else:
			return False

except:
	GOOGLE_AUTH = 0
	pass