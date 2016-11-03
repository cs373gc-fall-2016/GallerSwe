import os
#import model
import json
# from api import bind_api
import flask
import flask_sqlalchemy
import flask_restless
from flask import Flask, send_from_directory, render_template
from flask_cache import Cache

app = Flask(__name__, static_url_path='')

app.config["CACHE_TYPE"] = "null"

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cullenbounds@localhost/artsnob'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = flask_sqlalchemy.SQLAlchemy(app)
#bind_api(app)

@app.route('/')
def root():
    return app.send_static_file('index.html')

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)

# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Artist, methods=['GET'])


# DELETE THIS WHEN WE HAVE REAL API!!!
@app.route('/hack-api/artist')
def artists():
	with open('tempArtists.json') as json_data:
		artists = json.load(json_data)
	if artists is None :
		raise Exception
	return flask.jsonify(artists)

# DELETE THIS WHEN WE HAVE REAL API!!!
@app.route('/hack-api/artwork')
def artwork():
	with open('tempArtwork.json') as json_data:
		artwork = json.load(json_data)
	if artwork is None :
		raise Exception
	return flask.jsonify(artwork)

if __name__ == "__main__":
    app.run()
