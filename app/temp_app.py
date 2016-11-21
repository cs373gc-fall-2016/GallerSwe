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

app.config["CACHE_TYPE"] = "null"

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///artsnob'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = flask_sqlalchemy.SQLAlchemy(app)

