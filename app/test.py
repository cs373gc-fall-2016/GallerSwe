"""
Unit tests for modely.py
"""
from model import DB

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
        artist = Artist.query.all()
        self.assertEqual(len(artist), 1)

    def test_filteration1(self):
        """
        Test filtering 1
        """
        artist = Artist.query.filter(Artist.name == 'Andy Warhol')
        assertEqual(Artist.birth, 1900)

    def test_filteration2(self):
        """
        Test filtering 2
        """
        artist = Artist.query.filter(Artist.birth == 1900)
        assertEqual(artist.name, 'Andy Warhol')

    def test_addition_deletion(self):
        """
        Test adding and deleting
        """
        artist = Artist('2','Pablo Picasso', '1920', 'Male', 'Spain', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(artist)
        DB.session.commit()
        self.assertEqual(len(Artist.query.all()), 2)
        Ingredient.query.filter(Artist.name == 'Pablo Picasso').delete()
        DB.session.commit()
        self.assertEqual(len(Artist.query.all()), 1)




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
        artwork = Artwork.query.all()
        self.assertEqual(len(artwork), 1)

    def test_filteration1(self):
        """
        Test filtering 1
        """
        artwork = Artwork.query.filter(Artwork.name == 'Statue of David')
        assertEqual(artwork.medium, 'Statue')

    def test_filteration2(self):
        """
        Test filtering 2
        """        
        artwork = Artwork.query.filter(Artwork.medium == 'Statue')
        assertEqual(artwork.name, 'Statue of David')

    def test_addition_deletion(self):
        """
        Test adding and deleting
        """
        artowrk = Artowrk('2','Mona Lisa','paint', 'oil', '1800', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(artwork)
        DB.session.commit()
        self.assertEqual(len(Artwork.query.all()), 2)
        Artwork.query.filter(Artwork.name == 'Mona Lisa').delete()
        DB.session.commit()
        self.assertEqual(len(Artwork.query.all()), 1)



class Collection(TestCase):
    """
    Test cases for Collection
    """

    def test_insertion(self):
        """
        Test insertion
        """
        collect = Collection('1', 'National Museum of Art, Washington D.C.', 'http://www.nga.gov', 'North America', 'Institution')
        DB.session.add(location)

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
        collect = Collection.query.all()
        self.assertEqual(len(Collection), 1)

    def test_filteration1(self):
        """
        Test filtering 1
        """
        collect = Collection.query.filter(Collection.name == 'National Museum of Art, Washington D.C.')
        assertEqual(Collection.region, "North America")

    def test_filteration1(self):
        """
        Test filtering 2
        """  
        collect = Collection.query.filter(Collection.region == 'North America')
        assertEqual(Collection.name, 'National Museum of Art, Washington D.C.')

    def test_addition_deletion(self):
        """
        Test adding and deleting
        """
        collect = Collection('2','Kimbell Museum of Art','https://www.kimbellart.org', 'North America', 'Institution')
        DB.session.add(Collection)
        DB.session.commit()
        self.assertEqual(len(Collection.query.all()), 2)
        Collection.query.filter(Collection.name == 'Kimbell Museum of Art').delete()
        DB.session.commit()
        self.assertEqual(len(Collection.query.all()), 1)



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
        style = Style.query.all()
        self.assertEqual(len(style), 1)

    def test_filteration1(self):
        """
        Test filtering 1
        """
        style = Style.query.filter(Style.description == 'cool')
        assertEqual(style.name, 'Pop')

    def test_filteration2(self):
        """
        Test filtering 2
        """
        style = Style.query.filter(Style.name == 'Pop')
        assertEqual(style.description, 'cool')

    def test_addition_deletion(self):
        """
        Test adding and deleting
        """
        style = Style('2','Modern', 'kinda wierd', 'http://a5.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU1MTYxNzY3NDM5.jpg')
        DB.session.add(style)
        DB.session.commit()
        self.assertEqual(len(Style.query.all()), 2)
        Style.query.filter(Style.name == 'Modern').delete()
        DB.session.commit()
        self.assertEqual(len(Style.query.all()), 1)

# ----
# main
# ----
if __name__ == "__main__":
    main()
