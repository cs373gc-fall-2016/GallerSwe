import os

from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/artists')
def artists():
    return app.send_static_file('artists.html')

@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.route('/artwork')
def artwork():
    return app.send_static_file('artwork.html')

@app.route('/style')
def style():
    return app.send_static_file('style.html')

@app.route('/geo')
def geo():
    return app.send_static_file('geo.html')

@app.route('/temp')
def temp():
    info = {'Name': 'Andy_Warhol', 'Age': '49', 'Date': 'today'}
    return render_template('template.html',result=info)

if __name__ == "__main__":
    app.run()
