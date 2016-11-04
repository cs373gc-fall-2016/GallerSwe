"""
Unit tests for modely.py
"""

import unittest
from unittest import main, TestCase
from model import Artist, Artwork, Style, Collection, DB


class TestArtist(TestCase):
    """
    Test cases for Artist
    """
    def setUp(self):
        DB.drop_all()
        DB.create_all()
        artist1 = Artist('1','Andy Warhol', '1900', 'Male', 'American','http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(artist1)
        DB.session.commit()


    def tearDown(self):
        """
        Test deletion
        """
        DB.session.remove()
        DB.drop_all()

    def test_find_all(self):
        """
        Test finding all
        """
        artist = Artist.query.all()
        self.assertEqual(len(artist), 1)

    def test_filteration1(self):
        """
        Test filtering 1
        """
        artist = Artist.query.filter_by(name = 'Andy Warhol').first()
        self.assertEqual(artist.birth, '1900')

    def test_filteration2(self):
        """
        Test filtering 2
        """
        artist = Artist.query.filter_by(birth = '1900').first()
        self.assertEqual(artist.name, 'Andy Warhol')

    def test_addition_deletion(self):
        """
        Test adding and deleting
        """
        artist2 = Artist('2','Pablo Picasso', '1920', 'Male', 'Spain', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(artist2)
        DB.session.commit()
        self.assertEqual(len(Artist.query.all()), 2)
        Artist.query.filter_by(name = 'Pablo Picasso').delete()
        DB.session.commit()
        self.assertEqual(len(Artist.query.all()), 1)




class TestArtwork(TestCase):
    """
    Test cases for Artwork
    """
    def setUp(self):
        DB.drop_all()
        DB.create_all()
        artwork = Artwork('1','Statue of David', 'statue', 'Statue','1000', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(artwork)
        DB.session.commit()


    def tearDown(self):
        """
        Test deletion
        """
        DB.session.remove()
        DB.drop_all()

    def test_find_all(self):
        """
        Test finding all
        """
        artwork = Artwork.query.all()
        self.assertEqual(len(artwork), 1)

    def test_filteration1(self):
        """
        Test filtering 1
        """
        artwork = Artwork.query.filter_by(title = 'Statue of David').first()
        self.assertEqual(artwork.medium, 'Statue')

    def test_filteration2(self):
        """
        Test filtering 2
        """        
        artwork = Artwork.query.filter_by(medium = 'Statue').first()
        self.assertEqual(artwork.title, 'Statue of David')

    def test_addition_deletion(self):
        """
        Test adding and deleting
        """
        artwork = Artwork('2','Mona Lisa','paint', 'oil', '1800', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(artwork)
        DB.session.commit()
        self.assertEqual(len(Artwork.query.all()), 2)
        Artwork.query.filter_by(title = 'Mona Lisa').delete()
        DB.session.commit()
        self.assertEqual(len(Artwork.query.all()), 1)



class TestCollection(TestCase):
    """
    Test cases for Collection
    """
    def setUp(self):
        DB.drop_all()
        DB.create_all()
        collect = Collection('1', 'National Museum of Art', 'http://www.nga.gov', 'North America', 'Institution')
        DB.session.add(collect)
        DB.session.commit()

    def tearDown(self):
        """
        Test deletion
        """
        DB.session.remove()
        DB.drop_all()

    def test_find_all(self):
        """
        Test finding all
        """
        collect = Collection.query.all()
        self.assertEqual(len(collect), 1)

    def test_filteration1(self):
        """
        Test filtering 1
        """
        collect = Collection.query.filter_by(institution = 'National Museum of Art').first()
        self.assertEqual(collect.region, 'North America')

    def test_filteration1(self):
        """
        Test filtering 2
        """  
        collect = Collection.query.filter_by(region = 'North America').first()
        self.assertEqual(collect.institution, 'National Museum of Art')

    def test_addition_deletion(self):
        """
        Test adding and deleting
        """
        collect = Collection('2','Kimbell Museum of Art','https://www.kimbellart.org', 'North America', 'Institution')
        DB.session.add(collect)
        DB.session.commit()
        self.assertEqual(len(Collection.query.all()), 2)
        Collection.query.filter_by(institution = 'Kimbell Museum of Art').delete()
        DB.session.commit()
        self.assertEqual(len(Collection.query.all()), 1)



class TestStyle(TestCase):
    """
    Test cases for Style
    """
    def setUp(self):
        DB.drop_all()
        DB.create_all()
        style = Style('1','Pop', 'cool', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(style)
        DB.session.commit()

    def tearDown(self):
        """
        Test deletion
        """
        DB.session.remove()
        DB.drop_all()

    def test_find_all(self):
        """
        Test finding all
        """
        style = Style.query.all()
        self.assertEqual(len(style), 1)

    def test_filteration1(self):
        """
        Test filtering 1
        """
        style = Style.query.filter_by(description = 'cool').first()
        self.assertEqual(style.name, 'Pop')

    def test_filteration2(self):
        """
        Test filtering 2
        """
        style = Style.query.filter_by(name = 'Pop').first()
        self.assertEqual(style.description, 'cool')

    def test_addition_deletion(self):
        """
        Test adding and deleting
        """
        style = Style('2','Modern', 'kinda wierd', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(style)
        DB.session.commit()
        self.assertEqual(len(Style.query.all()), 2)
        Style.query.filter_by(name = 'Modern').delete()
        DB.session.commit()
        self.assertEqual(len(Style.query.all()), 1)

# ----
# main
# ----
if __name__ == "__main__":
    main()
