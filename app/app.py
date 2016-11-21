import os
#import model
import json
# from api import bind_api
import flask
import flask_sqlalchemy
import flask_restless
from flask import Flask, jsonify, send_from_directory, render_template
from flask_cache import Cache
from subprocess import *
from search import search

app = Flask(__name__, static_url_path='')

# app.config["CACHE_TYPE"] = "null"

# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///artsnob'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# DB = flask_sqlalchemy.SQLAlchemy(app)

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/search/<phrase>')
def search_phrase(phrase):

    results = search(phrase)
    return jsonify(results)

### endpoint used by about page to run unit tests ####
@app.route('/run-unit-tests')
def test():
    return run(["python3", "test.py", "--verbose"], stdout=PIPE, stderr=STDOUT, universal_newlines=True).stdout

if __name__ == "__main__":
    app.run()

