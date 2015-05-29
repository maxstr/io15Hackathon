__author__ = 'dirtbag'

from google.appengine.ext import db

class User(db.Model):
    user_name = db.StringProperty(required=True)
    user_email = db.EmailProperty(required=True)
    user_phone = db.StringProperty(required=True)
    address_street = db.StringProperty(required=True)
    address_street2 = db.StringProperty(required=True)
    address_city = db.StringProperty(required=True)
    address_state = db.StringProperty(required=True)
    address_zipcode = db.StringProperty(required=True)
    modified_date = db.DateTimeProperty(auto_now=True)

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid)

    @classmethod
    def GetByEmail(cls, email):
        user = User.all().filter('user_email =', email).get()
        return user
