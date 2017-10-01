import os

from flask import Flask
from flask_restful import Api

from cdc_app.extensions import db
from config import db_config


def generate_psql_url(config):
    """
    from a config return a psql_url
    :param config:
    :return:
    """
    url = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s'
    return url % config


def create_app():
    """
    create the cdc flask app
    :return: flask.Flask application
    """
    app = Flask(__name__)
    update_app_config(app)
    setup_db(app)

    api = Api(app)
    add_api_resources(api)

    return app


def setup_db(app):
    db.app = app
    db.init_app(app)


def update_app_config(app):
    """
    :param app: Flask() app object
    :return: nothing... it's a static method
    """
    # silly flask_restul requires an extra config
    # to minimize json responses... blah blah
    settings = app.config.get('RESTFUL_JSON', {})
    settings.setdefault('indent', None)
    settings.setdefault('sort_keys', True)


    app.config.update(
        DEBUG=os.environ.get('DEBUG', True),
        SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI', generate_psql_url(db_config)),
        SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False),
        JSONIFY_PRETTYPRINT_REGULAR=True,
        RESTFUL_JSON=settings
    )


def add_api_resources(api):
    # import necessary models
    from cdc_app.api.cdc import CDCSummary
    from cdc_app.api.cdc import CDCDataRecord

    # add each resource
    api.add_resource(
        CDCSummary,
        '/',
        '/summary',
    )

    api.add_resource(
        CDCDataRecord,
        '/cdc/resource/<id>'
    )
