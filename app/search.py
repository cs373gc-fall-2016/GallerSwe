from flask import Flask, jsonify
from model import Artist, Artwork, Style, Collection

APP = Flask(__name__)

def search(phrase):
    """
    Given a phrase to search, return json style object containing
    the results. Each result consists of a name, the
    attribute that the words appeared in, and the instance id.

    All results are separated by which model they are a part of.

    AND results will be put first followed by OR results
    """

    artists = Artist.query.all()
    artworks = Artwork.query.all()
    styles = Style.query.all()
    collections = Collection.query.all()

    andArtistResults = []
    for artist in artists:
        andArtistResults = get_artist_results(artist, phrase)

    andArtworkResults =[]
    for artwork in artworks:
        andArtworkResults = get_artwork_results(artwork, phrase)

    andStyleResults = []
    for style in styles:
        andStyleResults = get_style_results(style, phrase)

    andCollectionResults = []
    for collection in collections:
        andCollectionResults = get_collection_results(collection, phrase)

    andResults = {"artist results" : andArtistResults,
                  "artwork results" : andArtworkResults,
                  "style results" : andStyleResults,
                  "collection results" : andCollectionResults}

    orArtistResults = []
    orArtworkResults = []
    orStyleResults = []
    orCollectionResults = []
    words = phrase.split()
    for word in words:
        for artist in artists:
            orArtistResults.extend(get_artist_results(artist, word))

        for artwork in artworks:
            orArtworkResults.extend(get_artwork_results(artwork, word))

        for style in styles:
            orStyleResults.extend(get_style_results(style, word))

        for collection in collections:
            orCollectionResults.extend(get_collection_results(collection, word))

    orResults = {"artist results" : orArtistResults,
                  "artwork results" : orArtworkResults,
                  "style results" : orStyleResults,
                  "collection results" : orCollectionResults}

    return {"and results" : andResults, "or results" : orResults}

def get_artist_results(artist, phrase):
    """
    Search the artist's attributes for a phrase
    and return list of the results
    """
    results = []
    phrase = phrase.lower()
    if artist.name.lower().find(phrase) != -1:
        results.append({"name"    : artist.name,
                        "context" : "Name: " + artist.name,
                        "id"      : artist.id})

    if artist.gender.lower().find(phrase) != -1:
        results.append({"name"    : artist.name,
                        "context" : "Gender: " + artist.gender,
                        "id"      : artist.id})

    if artist.birth.lower().find(phrase) != -1:
        results.append({"name"    : artist.name,
                        "context" : "Birth Year: " + artist.birth,
                        "id"      : artist.id})

    if artist.hometown.lower().find(phrase) != -1:
        results.append({"name"    : artist.name,
                        "context" : "Birth Place: " + artist.hometown,
                        "id"      : artist.id})

    return results

def get_artwork_results(artwork, phrase):
    """
    Search the artwork's attributes for a phrase
    and return list of the results
    """
    results = []
    phrase = phrase.lower()
    if artwork.title.lower().find(phrase) != -1:
        results.append({"title"    : artwork.title,
                        "context" : "Title: " + artwork.title,
                        "id"      : artwork.id})

    if artwork.date.lower().find(phrase) != -1:
        results.append({"title"    : artwork.title,
                        "context" : "Date: " + artwork.date,
                        "id"      : artwork.id})

    if artwork.medium.lower().find(phrase) != -1:
        results.append({"title"    : artwork.title,
                        "context" : "Medium: " + artwork.medium,
                        "id"      : artwork.id})

    return results

def get_style_results(style, phrase):
    """
    Search the style's attributes for a phrase
    and return list of the results
    """
    results = []
    phrase = phrase.lower()
    if style.name.lower().find(phrase) != -1:
        results.append({"name"    : style.name,
                        "context" : "Name: " + style.name,
                        "id"      : style.id})

    if style.description.lower().find(phrase) != -1:
        results.append({"name"    : style.name,
                        "context" : "Description: " + style.description,
                        "id"      : style.id})

    return results

def get_collection_results(collection, phrase):
    """
    Search the collection's attributes for a phrase
    and return list of the results
    """
    results = []
    phrase = phrase.lower()
    if collection.institution.lower().find(phrase) != -1:
        results.append({"name"    : collection.institution,
                        "context" : "Name: " + collection.institution,
                        "id"      : collection.id})

    if collection.website.lower().find(phrase) != -1:
        results.append({"name"    : collection.institution,
                        "context" : "Website: " + collection.website,
                        "id"      : collection.id})

    if collection.reion.lower().find(phrase) != -1:
        results.append({"name"    : collection.institution,
                        "context" : "Region: " + collection.region,
                        "id"      : collection.id})

    return results

if __name__ == "__main__":
    APP.run()
