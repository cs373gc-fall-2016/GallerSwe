"""
DB for Artsnob

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.DB'
DB = SQLAlchemy(APP)


GEOREG_STYLE = DB.Table(
    'georegstyle', DB.Column(
        'georegId', DB.Integer, DB.ForiegnKey('georeg.georegid')), DB.Column(
            'styleId', DB.Integer, DB.ForiegnKey('style.styleid')))

ARTIST_STYLE = DB.Table(
    'artiststyle', DB.Column(
        'artistId', DB.Integer, DB.ForiegnKey('artist.artistid')), DB.Column(
            'styleId', DB.Integer, DB.ForiegnKey('style.styleid')))

GEOREG_ARTIST = DB.Table(
    'georegartist', DB.Column(
        'georegId', DB.Integer, DB.ForiegnKey('georeg.georegid')), DB.Column(
            'artistId', DB.Integer, DB.ForiegnKey('artist.artistid')))

# artist_artist = DB.Table('artist_artist',
# 	DB.Column('artist_id', DB.Integer, DB.ForiegnKey('artist.id')),
# 	DB.Column('artist_id', DB.Integer, DB.ForiegnKey('artist_id'))
# 	)


class Artist(DB.Model):
    _tablename_ = 'artist'
    artistid = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String)
    description = DB.Column(DB.String)
    birth = DB.Column(DB.Integer)
    death = DB.Column(DB.Integer)
    artwork = DB.relationship('Work', backref='artist', lazy='dynamic')
    nationality = DB.relationship('Nationality', secondary=GEOREG_ARTIST,
                                  backref=DB.backref('artist', lazy='dynamic'))
    style = DB.relationship('Style', secondary=ARTIST_STYLE,
                            backref=DB.backref('artist', lazy='dynamic'))

    # def __init__(self, name, description, birth, death):
    # 	self.name = name
    # 	self.description = description
    # 	self.birth = birth
    # 	self.death = death

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
    artworkid = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String)
    medium = DB.Column(DB.String)
    description = DB.Column(DB.String)
    georeg = DB.relationship('GeoReg', backref='person', lazy='dynamic')
    artist_id = DB.Column(DB.String, DB.ForiegnKey('artist.artistid'))

    # def __init__(self, name, medium, description):
    # 	self.name = name
    # 	self.medium = medium
    # 	self.description = description


class GeoReg(DB.Model):
    __tablename__ = 'georeg'
    georegid = DB.Column(DB.Integer, primary_key=True)
    location = DB.Column(DB.String)
    artwork = DB.Column(DB.Integer, DB.ForiegnKey('artwork.artworkid'))
    style = DB.relationship('style', secondary=GEOREG_STYLE,
                            backref=DB.backref('georeg', lazy='dynamic'))



class Style(DB.Model):
    __tablename__ = 'style'
    styleid = DB.Column(DB.Integer, primary_key=True)
    description = DB.Column(DB.String)
    time_period = DB.Column(DB.String)
