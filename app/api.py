from flask_restless import APIManager
from model import Artist, Artwork, Style, Collection


def bind_api(app):
    """ Bind the api to the app """
    api = APIManager(app, flask_sqlalchemy_db=model.db)

    api.create_api(
        model.Artist,
        collection_name='artist',
        url_prefix='/api/',
        include_columns=[
            'id',
            'name',
            'gender',
            'birthday',
            'hometown',
            'artworks',
            'thumbnail',
        ]
    )

    api.create_api(
        model.Artwork,
        collection_name='artwork',
        url_prefix='/api/',
        include_columns=[
            'id',
            'title',
            'category',
            'medium',
            'date',
            'artists',
            'styles',
            'thumbnail',
        ]
    )

    api.create_api(
        model.Style,
        collection_name='style',
        url_prefix='/api/',
        include_columns=[
            'id',
            'name',
            'description',
            'artworks',
            'number_of_artists',
            'thumbnail',
        ]
    )

    api.create_api(
        model.Collection,
        collection_name='collection',
        url_prefix='/api/',
        include_columns=[
            'id',
            'type',
            'name',
            'artworks',
            'website',
        ]
    )

    manager.init_app(app)