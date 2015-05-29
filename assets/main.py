
# title:	bootsmooth demo app for appengine
# date:		2015-MAY-16

from flask import Flask
import flask.ext.sqlalchemy
import flask.ext.restless



# create our flask app object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = flask.ext.sqlalchemy.SQLAlchemy(app)

# Route all URL patterns to the a controller
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    email = db.Column(db.Text)
    phone = db.Column(db.Text)

class UserProduce(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    number = db.Column(db.Integer)
    produceID = db.Column(db.Integer, db.ForeignKey('produce.id'))

class PickLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    produceID = db.Column(db.Integer, db.ForeignKey('produce.id'))
    date = db.Column(db.Date)

class Produce(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    season = db.Column(db.Text)

db.create_all()
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(User, methods=['GET', 'POST', 'DELETE'])



# http error handlers
@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
	"""Return a custom 500 error."""
	return 'Sorry, unexpected error: {}'.format(e), 500
