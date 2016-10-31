"""
DB for Artsnob

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root@localhost/artsnob'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)

ID_CHARS = 24
NAME_CHARS = 255
DATE_CHARS = 64
DESC_CHARS = 1000

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
    artworks = DB.relationship('Artwork', back_populates='artists', secondary=ARTWORK_ARTIST)

    def __init__(self, id, name, birth):
        self.id = id
        self.name = name
        self.birth = birth

    
    # def dictionary(self):
    # 	asdict = {}
    # 	asdict['id'] = self.id
    # 	asdict['name'] = self.name
    # 	asdict['description'] = self.description
    # 	asdict['birth'] = self.birth
    # 	asdict['death'] = self.death
    # 	artwork = list(self.artwork)
    # 	style = list(self.style)
    # 	georeg = list(self.georeg)
    # 	if artwork:
    # 		asdict['artwork_id'] = [ar.id for ar in artwork]
    # 	if style:
    # 		asdict['style'] = [s.name for s in style]
    # 	if georeg:
    # 		asdict['nationality'] = [g.name for g in georeg]
    # 	return asdict

class Artwork(DB.Model):
    """
    The artwork model contains attributes about an artwork such as
    name, medium, description, and style
    """
    __tablename__ = 'artwork'
    id = DB.Column(DB.String(ID_CHARS), primary_key=True)
    title = DB.Column(DB.String(NAME_CHARS))
    medium = DB.Column(DB.String(DESC_CHARS))
    description = DB.Column(DB.String(DESC_CHARS))
    artists = DB.relationship('Artist', back_populates='artworks',
                              secondary=ARTWORK_ARTIST)
    styles = DB.relationship('Style', back_populates='artworks',
                             secondary=ARTWORK_STYLE)
    collections = DB.relationship('Collection', back_populates='artworks',
                                  secondary=ARTWORK_COLLECTION)

    def __init__(self, id, title, medium, description):
        self.id = id
        self.title = title
        self.medium = medium
        self.description = description


class Collection(DB.Model):
    """
    """
    __tablename__ = 'collection'
    id = DB.Column(DB.String(ID_CHARS), primary_key=True)
    name = DB.Column(DB.String(NAME_CHARS))
    location = DB.Column(DB.String(DESC_CHARS))
    public = DB.Boolean()
    artworks = DB.relationship('Artwork', back_populates='collections',
                               secondary=ARTWORK_COLLECTION)

    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

class Style(DB.Model):
    """
    The style model contains attributes about a style such as
    name, description and time period
    """
    __tablename__ = 'style'
    id = DB.Column(DB.String(ID_CHARS), primary_key=True)
    name = DB.Column(DB.String(NAME_CHARS))
    description = DB.Column(DB.String)
    time_period = DB.Column(DB.String)
    artworks = DB.relationship('Artwork', back_populates='styles', secondary=ARTWORK_STYLE)

    def __init__(self, id, name, description, time_period):
        self.id = id
        self.name = name
        self.description = description
        self.time_period = time_period
