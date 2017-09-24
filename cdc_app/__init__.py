import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

__db__ = {
    'user': 'kmacneneyjr',
    'pw': '',
    'db': 'cdc_data',
    'host': 'localhost',
    'port': '5432',
}


def generate_psql_url(config):
    """
    from a config return a psql_url
    :param config:
    :return:
    """
    url = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s'
    return url % config


def create_cdc_app():
    """
    create the cdc flask app
    :return: flask.Flask application
    """
    app = Flask(__name__)
    app.config.update(
        DEBUG=os.environ.get('DEBUG', True),
        SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI', generate_psql_url(__db__)),
        SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    )
    db.init_app(app)

    from cdc_app.cdc import CDCSummary

    api = Api(app)
    api.add_resource(
        CDCSummary,
        '/',
        '/summary'
    )

    return app
