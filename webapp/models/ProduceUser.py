__author__ = 'dirtbag'

from google.appengine.ext import db

class ProduceUser(db.Model):
    user_email = db.EmailProperty(required=True)
    produce_name = db.StringProperty(required=True)
    produce_quantity = db.IntegerProperty(required=True)
    modified_date = db.DateTimeProperty(auto_now=True)

    @classmethod
    def by_id(cls, uid):
        return ProduceUser.get_by_id(uid)

    @classmethod
    def by_email(cls, email):
        produceList = ProduceUser.all().filter('user_email =', email).get()

        return produceList
