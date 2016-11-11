import os
#import model
import json
# from api import bind_api
import flask
import flask_sqlalchemy
import flask_restless
from flask import Flask, send_from_directory, render_template
from flask_cache import Cache
import subprocess

app = Flask(__name__, static_url_path='')

# app.config["CACHE_TYPE"] = "null"

# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///artsnob'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# DB = flask_sqlalchemy.SQLAlchemy(app)

@app.route('/')
def root():
    return app.send_static_file('index.html')

### endpoint used by about page to run unit tests ####
@app.route('/run-unit-tests')
def test():
    proc = subprocess.Popen(["python3 test.py"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out

if __name__ == "__main__":
    app.run()

