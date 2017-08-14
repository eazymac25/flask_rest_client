import json
from rest_client.db_config import db_config, generate_sql_url
from flask import Flask, request
from flask_restful import Api, Resource
from rest_client.models import db, NycAirData, BaseModel

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = generate_sql_url(db_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def main():
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


if __name__ == '__main__':

    app.config['DEBUG'] = True
    app.run()
