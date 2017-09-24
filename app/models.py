import datetime

from app import db


class BaseModel(db.Model):
    """
    This is a doc comment
    """
    # TODO: Fix comments

    __abstract__ = True

    def __init__(self, *args):
        super(BaseModel, self).__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self.__dict__.items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self.__dict__.items()
        }


class NycAirData(BaseModel, db.Model):

    __tablename__ = 'nyc_air_data'

    key = db.Column(db.Integer, primary_key=True)
    indicator_data_id = db.Column(db.Integer)
    indicator_id = db.Column(db.Integer)
    name = db.Column(db.Text)
    Measure = db.Column(db.Text)
    geo_type_name = db.Column(db.Text)
    geo_entity_id = db.Column(db.Integer)
    geo_entity_name = db.Column(db.Text)
    year_description = db.Column(db.Text)
    data_valuemessage = db.Column(db.Text)

    def __init__(self):
        super(NycAirData, self).__init__()

