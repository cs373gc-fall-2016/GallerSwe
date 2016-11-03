"""
Unit tests for modely.py
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/artsnob'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)

import unittest
from unittest import main, TestCase
from model import Artist, Artwork, Style, Collection





class TestArtist(TestCase):
    """
    Test cases for Artist
    """

    def test_insertion(self):
        """
        Test insertion
        """
        DB.create_all()
        artist1 = Artist('1','Andy Warhol', '1900', 'Male', 'American','http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(artist1)

    def test_deletion(self):
        """
        Test deletion
        """
        DB.session.remove()
        DB.drop_all()

    def test_find_all(self):
        """
        Test finding all
        """
        artist = DB.session.query.all()
        self.assertEqual(len(artist), 1)

    def test_filteration1(self):
        """
        Test filtering 1
        """
        artist = DB.session.query.filter(Artist.name == 'Andy Warhol')
        assertEqual(artist.birth, 1900)

    def test_filteration2(self):
        """
        Test filtering 2
        """
        artist = DB.session.query.filter(Artist.birth == 1900)
        assertEqual(artist.name, 'Andy Warhol')

    def test_addition_deletion(self):
        """
        Test adding and deleting
        """
        artist2 = Artist('2','Pablo Picasso', '1920', 'Male', 'Spain', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(artist2)
        DB.session.commit()
        self.assertEqual(len(DB.session.query.all()), 2)
        DB.session.query.filter(Artist.name == 'Pablo Picasso').delete()
        DB.session.commit()
        self.assertEqual(len(DB.session.query.all()), 1)




class TestArtwork(TestCase):
    """
    Test cases for Artwork
    """

    def test_insertion(self):
        """
        Test insertion
        """
        DB.create_all()
        artwork = Artwork('1','Statue of David', 'statue', 'Statue','1000', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(artwork)

    def test_deletion(self):
        """
        Test deletion
        """
        DB.session.remove()
        DB.drop_all()

    def test_find_all(self):
        """
        Test finding all
        """
        artwork = DB.session.query.all()
        self.assertEqual(len(artwork), 1)

    def test_filteration1(self):
        """
        Test filtering 1
        """
        artwork = DB.session.query.filter(Artwork.name == 'Statue of David')
        assertEqual(artwork.medium, 'Statue')

    def test_filteration2(self):
        """
        Test filtering 2
        """        
        artwork = DB.session.query.filter(Artwork.medium == 'Statue')
        assertEqual(artwork.name, 'Statue of David')

    def test_addition_deletion(self):
        """
        Test adding and deleting
        """
        artowrk = Artowrk('2','Mona Lisa','paint', 'oil', '1800', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(artwork)
        DB.session.commit()
        self.assertEqual(len(DB.session.query.all()), 2)
        DB.session.query.filter(Artwork.name == 'Mona Lisa').delete()
        DB.session.commit()
        self.assertEqual(len(DB.session.query.all()), 1)



class Collection(TestCase):
    """
    Test cases for Collection
    """

    def test_insertion(self):
        """
        Test insertion
        """
        collect = Collection('1', 'National Museum of Art, Washington D.C.', 'http://www.nga.gov', 'North America', 'Institution')
        DB.session.add(collect)

    def test_deletion(self):
        """
        Test deletion
        """
        DB.session.remove()
        DB.drop_all()

    def test_find_all(self):
        """
        Test finding all
        """
        collect = DB.session.query.all()
        self.assertEqual(len(collect), 1)

    def test_filteration1(self):
        """
        Test filtering 1
        """
        collect = DB.session.query.filter(Collection.name == 'National Museum of Art, Washington D.C.')
        assertEqual(collect.region, "North America")

    def test_filteration1(self):
        """
        Test filtering 2
        """  
        collect = DB.session.query.filter(Collection.region == 'North America')
        assertEqual(collect.name, 'National Museum of Art, Washington D.C.')

    def test_addition_deletion(self):
        """
        Test adding and deleting
        """
        collect = Collection('2','Kimbell Museum of Art','https://www.kimbellart.org', 'North America', 'Institution')
        DB.session.add(collect)
        DB.session.commit()
        self.assertEqual(len(DB.session.query.all()), 2)
        DB.session.query.filter(Collection.name == 'Kimbell Museum of Art').delete()
        DB.session.commit()
        self.assertEqual(len(DB.session.query.all()), 1)



class TestStyle(TestCase):
    """
    Test cases for Style
    """

    def test_insertion(self):
        """
        Test insertion
        """
        DB.create_all()
        style = Style('1','Pop', 'cool', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(style)

    def test_deletion(self):
        """
        Test deletion
        """
        DB.session.remove()
        DB.drop_all()

    def test_find_all(self):
        """
        Test finding all
        """
        style = DB.session.query.all()
        self.assertEqual(len(style), 1)

    def test_filteration1(self):
        """
        Test filtering 1
        """
        style = DB.session.query.filter(Style.description == 'cool')
        assertEqual(style.name, 'Pop')

    def test_filteration2(self):
        """
        Test filtering 2
        """
        style = DB.session.query.filter(Style.name == 'Pop')
        assertEqual(style.description, 'cool')

    def test_addition_deletion(self):
        """
        Test adding and deleting
        """
        style = Style('2','Modern', 'kinda wierd', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(style)
        DB.session.commit()
        self.assertEqual(len(DB.session.query.all()), 2)
        DB.session.query.filter(Style.name == 'Modern').delete()
        DB.session.commit()
        self.assertEqual(len(DB.session.query.all()), 1)

# ----
# main
# ----
if __name__ == "__main__":
    main()
