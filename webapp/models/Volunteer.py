__author__ = 'dirtbag'

from google.appengine.ext import db

class Volunteer(db.Model):
    volunteer_name = db.StringProperty(required=True)
    volunteer_email = db.EmailProperty(required=True)
    volunteer_phone = db.StringProperty(required=True)
    address_street = db.StringProperty(required=True)
    address_street2 = db.StringProperty(required=True)
    address_city = db.StringProperty(required=True)
    address_state = db.StringProperty(required=True)
    address_zipcode = db.StringProperty(required=True)
    modified_date = db.DateTimeProperty(auto_now=True)

    @classmethod
    def by_id(cls, uid):
        return Volunteer.get_by_id(uid)

    @classmethod
    def GetByEmail(cls, email):
        volunteer = Volunteer.all().filter('volunteer_email =', email).get()
        return volunteer
