import os
#import model
import json

from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return render_template('splash.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/artists')
def artists():
	with open('tempArtists.json') as json_data:
		artists = json.load(json_data)
	if artists is None :
		raise Exception
	return render_template('artists.html', result=artists)

# @app.route('/artists/<int: id>')
# def artist(id) :
#     data = models.Artist.query.get(id)
#     if data is None :
#         raise Exception
#     return render_template("artist.html", result=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/artworks')
def artworks():
	with open('tempArtwork.json') as json_data:
		artworks = json.load(json_data)
	if artworks is None :
		raise Exception
	return render_template('artwork.html', result=artworks)

# @app.route('/artwork/<int: id>')
# def artwork(id) :
#     data = models.Artwork.query.get(id)
#     if data is None :
#         raise Exception
#     return render_template("artwork.html", result=data)

@app.route('/styles')
def styles():
    return render_template('style.html')

# @app.route('/style/<int: id>')
# def style(id) :
#     data = models.Style.query.get(id)
#     if data is None :
#         raise Exception
#     return render_template("style.html", result=data)

@app.route('/collections')
def collections():
    return render_template('collections.html')

# @app.route('/collections/<int: id>')
# def collection(id) :
#     data = models.Collection.query.get(id)
#     if data is None :
#         raise Exception
#     return render_template("collection.html", result=data)

@app.route('/temp')
def temp():
    info = {'Name': 'Andy_Warhol', 'Age': '49', 'Date': 'today'}
    return render_template('template.html',result=info)

if __name__ == "__main__":
    app.run()
