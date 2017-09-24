import json

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from instance.config import db_config, generate_sql_url


db = SQLAlchemy()


def create_app():

    from app.models import NycAirData

    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = generate_sql_url(db_config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    db.init_app(app)

    @app.route('/')
    def get_top_10():
        data = NycAirData()
        all_rows = data.query.limit(10).all()
        l = []
        for row in all_rows:
            d = {}
            for k, v in row.__dict__.items():
                if k[0] != '_':
                    d[k] = v
            l.append(d)
        return json.dumps(l)

    return app
