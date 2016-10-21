"""
Unit tests for modely.py
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config')

db = SQLAlchemy(app)
import unittest
from unittest import main, TestCase
from models import Artist, Artwork, Style, GeoReg


"""
Test cases for Artist
"""


class TestArtist(TestCase):

    def create(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        return app

    def insertion(self):
        db.create_all()
        artist1 = Artist('Andy Warhol', 'cool guy', 1900, 1977)
        db.session.add(artist1)

    def deletion(self):
        db.session.remove()
        db.drop_all()

    def find_all(self):
        artist = Artist.query.all()
        self.assertEqual(len(artist), 1)

    def filteration1(self):
        artist = Artist.query.filter(Artist.name == 'Andy Warhol')
        assertEqual(Artist.birth, 1900)

    def filteration2(self):
        artist = Artist.query.filter(Artist.birth == 1900)
        assertEqual(artist.name, 'Andy Warhol')

    def additionDeletion(self):
        artist = Artist('Pablo Picasso', 'famous', 1920, 2000)
        db.session.add(artist)
        db.session.commit()
        self.assertEqual(len(Artist.query.all()), 2)
        Ingredient.query.filter(Artist.name == 'Pablo Picasso').delete()
        db.session.commit()
        self.assertEqual(len(Artist.query.all()), 1)

"""
Test cases for Artwork
"""


class TestArtwork(TestCase):

    def create(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        return app

    def insertion(self):
        db.create_all()
        artwork = Recipe('Statue of David', 'statue', 'cool guy')
        db.session.add(artwork)

    def deletion(self):
        db.session.remove()
        db.drop_all()

    def find_all(self):
        artwork = Artwork.query.all()
        self.assertEqual(len(artwork), 1)

    def filteration1(self):
        artwork = Artwork.query.filter(Artwork.name == 'Statue of David')
        assertEqual(artwork.medium, 'statue')

    def filteration2(self):
        artwork = Artwork.query.filter(Artwork.medium == 'statue')
        assertEqual(artwork.name, 'Statue of David')

    def additionDeletion(self):
        artowrk = Artowrk('Mona Lisa', 'paint', 'cool lady')
        db.session.add(artwork)
        db.session.commit()
        self.assertEqual(len(Artwork.query.all()), 2)
        Artwork.query.filter(Artwork.name == 'Mona Lisa').delete()
        db.session.commit()
        self.assertEqual(len(Artwork.query.all()), 1)

"""
Test cases for GeoReg
"""


class GeoReg(TestCase):

    def create(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        return app

    def insertion(self):
        db.create_all()
        location = GeoReg('Africa')
        db.session.add(location)

    def deletion(self):
        db.session.remove()
        db.drop_all()

    def find_all(self):
        georeg = GeoReg.query.all()
        self.assertEqual(len(georeg), 1)

    def filteration1(self):
        georeg = GeoReg.query.filter(GeoReg.name == 'Africa')
        assertEqual(georeg.name, GeoReg)

    def additionDeletion(self):
        georeg = GeoReg('Middle East')
        db.session.add(georeg)
        db.session.commit()
        self.assertEqual(len(GeoReg.query.all()), 2)
        GeoReg.query.filter(GeoReg.name == 'Africa').delete()
        db.session.commit()
        self.assertEqual(len(GeoReg.query.all()), 1)

"""
Test cases for Style
"""


class TestStyle(TestCase):

    def create(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        return app

    def insertion(self):
        db.create_all()
        style = Style('Pop', 'cool', '1950')
        db.session.add(style)

    def deletion(self):
        db.session.remove()
        db.drop_all()

    def find_all(self):
        style = Style.query.all()
        self.assertEqual(len(style), 1)

    def filteration1(self):
        style = Style.query.filter(Style.time_period == '1950')
        assertEqual(style.name, 'Pop')

    def filteration2(self):
        style = Style.query.filter(Style.name == 'Pop')
        assertEqual(style.time_period, '1950')

    def additionDeletion(self):
        style = Style('Modern', 'kinda wierd', '2000')
        db.session.add(style)
        db.session.commit()
        self.assertEqual(len(Style.query.all()), 2)
        Style.query.filter(Style.name == 'Modern').delete()
        db.session.commit()
        self.assertEqual(len(Style.query.all()), 1)

# ----
# main
# ----
if __name__ == "__main__":
    main()
