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

# @app.route('/hello')
# def hello():
#     return render_template('hello.html')

@app.route('/hack-api/artist')
def artists():
	with open('tempArtists.json') as json_data:
		artists = json.load(json_data)
	if artists is None :
		raise Exception
	return flask.jsonify(artists)

# @app.route('/<string:id>')
# def detail(id) :
# 	with open('tempWarhol.json') as json_data:
# 		data = json.load(json_data)
# 	if data is None :
# 		raise Exception
# 	return render_template("detail.html", result=data)

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/artworks')
# def artworks():
# 	with open('tempArtwork.json') as json_data:
# 		artworks = json.load(json_data)
# 	if artworks is None :
# 		raise Exception
# 	return render_template('artwork.html', result=artworks)

# # @app.route('/artwork/<int: id>')
# # def artwork(id) :
# #     data = models.Artwork.query.get(id)
# #     if data is None :
# #         raise Exception
# #     return render_template("artwork.html", result=data)

# @app.route('/styles')
# def styles():
#     return render_template('style.html')

# # @app.route('/style/<int: id>')
# # def style(id) :
# #     data = models.Style.query.get(id)
# #     if data is None :
# #         raise Exception
# #     return render_template("style.html", result=data)

# @app.route('/collections')
# def collections():
#     return render_template('collections.html')

# # @app.route('/collections/<int: id>')
# # def collection(id) :
# #     data = models.Collection.query.get(id)
# #     if data is None :
# #         raise Exception
# #     return render_template("collection.html", result=data)

# @app.route('/temp')
# def temp():
#     info = {'Name': 'Andy_Warhol', 'Age': '49', 'Date': 'today'}
#     return render_template('template.html',result=info)

if __name__ == "__main__":
    app.run()
