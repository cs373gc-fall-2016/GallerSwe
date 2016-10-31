import os
import models

from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/artists')
def artists():
    return app.send_static_file('artists.html')

@app.route('/artists/<int: id>')
def artist(id) :
    data = models.Artist.query.get(id)
    if data is None :
        raise Exception
    return render_template("artist.html", result=data)

@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.route('/artworks')
def artworks():
    return app.send_static_file('artwork.html')

@app.route('/artwork/<int: id>')
def artwork(id) :
    data = models.Artwork.query.get(id)
    if data is None :
        raise Exception
    return render_template("artwork.html", result=data)

@app.route('/styles')
def styles():
    return app.send_static_file('style.html')

@app.route('/style/<int: id>')
def style(id) :
    data = models.Style.query.get(id)
    if data is None :
        raise Exception
    return render_template("style.html", result=data)

@app.route('/collections')
def collections():
    return app.send_static_file('collections.html')

@app.route('/collections/<int: id>')
def collection(id) :
    data = models.Collection.query.get(id)
    if data is None :
        raise Exception
    return render_template("collection.html", result=data)

@app.route('/temp')
def temp():
    info = {'Name': 'Andy_Warhol', 'Age': '49', 'Date': 'today'}
    return render_template('template.html',result=info)

if __name__ == "__main__":
    app.run()
