"""
DB for Artsnob
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

os.system('createdb testdb')
APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///testdb'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)

ID_CHARS = 24
NAME_CHARS = 255
DATE_CHARS = 64
GENDER_CHARS = 6
DESC_CHARS = 1000
LINK_CHARS = 255

ARTWORK_ARTIST = DB.Table('artist_artwork',
                          DB.Column('artist_id', DB.String(ID_CHARS),
                                    DB.ForeignKey('artist.id')),
                          DB.Column('artwork_id', DB.String(ID_CHARS),
                                    DB.ForeignKey('artwork.id')))

ARTWORK_COLLECTION = DB.Table('artwork_collection',
                              DB.Column('artwork_id', DB.String(ID_CHARS),
                                        DB.ForeignKey('artwork.id')),
                              DB.Column('collection_id', DB.String(ID_CHARS),
                                        DB.ForeignKey('collection.id')))

ARTWORK_STYLE = DB.Table('artworkstyle',
                         DB.Column('artwork_id', DB.String(ID_CHARS),
                                   DB.ForeignKey('artwork.id')),
                         DB.Column('style_id', DB.String(ID_CHARS),
                                   DB.ForeignKey('style.id')))


class Artist(DB.Model):
    """
    The artist model contains attributes about an artist such as
    name and birth date. Artists have a number of Artworks.
    To get the styles of an artist, filter the ARTWORK_STYLE table
    with all of their artworks.
    """
    _tablename_ = 'artist'
    id = DB.Column(DB.String(ID_CHARS), primary_key=True)
    name = DB.Column(DB.String(NAME_CHARS))
    birth = DB.Column(DB.String(DATE_CHARS))
    gender = DB.Column(DB.String(GENDER_CHARS))
    hometown = DB.Column(DB.String(NAME_CHARS))
    image = DB.Column(DB.String(LINK_CHARS))
    artworks = DB.relationship(
        'Artwork', back_populates='artists', secondary=ARTWORK_ARTIST)

    def __init__(self, id, name, birth, gender, nationality, image):
        self.id = id
        self.name = name
        self.birth = birth
        self.gender = gender
        self.hometown = hometown
        self.image = image

    def __repr__(self):
        return '<User %r>' % self.name


class Artwork(DB.Model):
    """
    The artwork model contains attributes about an artwork such as
    name, medium, description, and style
    """
    __tablename__ = 'artwork'
    id = DB.Column(DB.String(ID_CHARS), primary_key=True)
    title = DB.Column(DB.String(NAME_CHARS))
    category = DB.Column(DB.String(NAME_CHARS))
    medium = DB.Column(DB.String(DESC_CHARS))
    date = DB.Column(DB.String(DATE_CHARS))
    image = DB.Column(DB.String(LINK_CHARS))
    artists = DB.relationship('Artist', back_populates='artworks',
                              secondary=ARTWORK_ARTIST)
    styles = DB.relationship('Style', back_populates='artworks',
                             secondary=ARTWORK_STYLE)
    collections = DB.relationship('Collection', back_populates='artworks',
                                  secondary=ARTWORK_COLLECTION)

    def __init__(self, id, title, category, medium, date, image):
        self.id = id
        self.title = title
        self.category = category
        self.medium = medium
        self.date = date
        self.image = image

    def __repr__(self):
        return '<User %r>' % self.title


class Collection(DB.Model):
    """
    The collection model contains attributes about
    where a piece is located, the website of the institution,
    and the type of institution
    """
    __tablename__ = 'collection'
    id = DB.Column(DB.String(ID_CHARS), primary_key=True)
    institution = DB.Column(DB.String(NAME_CHARS))
    website = DB.Column(DB.String(LINK_CHARS))
    region = DB.Column(DB.String(NAME_CHARS))
    type = DB.Column(DB.String(NAME_CHARS))
    artworks = DB.relationship('Artwork', back_populates='collections',
                               secondary=ARTWORK_COLLECTION)

    def __init__(self, id, institution, website, region, ins_type):
        self.id = id
        self.institution = institution
        self.website = website
        self.region = region
        self.ins_type = ins_type

    def __repr__(self):
        return '<User %r>' % self.institution


class Style(DB.Model):
    """
    The style model contains attributes about a style such as
    name, description and time period
    """
    __tablename__ = 'style'
    id = DB.Column(DB.String(ID_CHARS), primary_key=True)
    name = DB.Column(DB.String(NAME_CHARS))
    description = DB.Column(DB.String)
    image = DB.Column(DB.String(LINK_CHARS))
    artworks = DB.relationship(
        'Artwork', back_populates='styles', secondary=ARTWORK_STYLE)

    def __init__(self, id, name, description, image):
        self.id = id
        self.name = name
        self.description = description
        self.image = image

    def __repr__(self):
        return '<User %r>' % self.name

DB.create_all()

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(APP, flask_sqlalchemy_db=DB)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Artist, methods=['GET'])
manager.create_api(Artwork, methods=['GET'])
manager.create_api(Style, methods=['GET'])
manager.create_api(Collection, methods=['GET'])

if __name__ == "__main__":
    APP.run()
