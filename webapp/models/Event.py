__author__ = 'dirtbag'

from google.appengine.ext import db

class Event(db.Model):
    user_email = db.EmailProperty(required=True)
    event_time = db.TimeProperty(required=True)
    event_note = db.StringProperty(required=True)
    modified_date = db.DateTimeProperty(auto_now=True)

    @classmethod
    def by_id(cls, uid):
        return Event.get_by_id(uid)

    @classmethod
    def by_email(cls, email):
        eventList = Event.all().filter('user_email =', email).get()

        return eventList
