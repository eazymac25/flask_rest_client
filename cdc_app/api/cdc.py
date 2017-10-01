from flask_restful import Resource, reqparse
from flask import jsonify

from cdc_app.model.cdc_chronic_raw import CdcChronicRaw

conn = CdcChronicRaw()


class CDCSummary(Resource):

    def __init__(self):
        super(CDCSummary, self).__init__()

    def get(self):
        cols = conn.get_table_summary()
        response = {
            "rowCount": conn.query.count(),
            "columnNames": [
                col for col in cols
            ]
        }
        return response, 201


class CDCDataRecord(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int)
        super(CDCDataRecord, self).__init__()

    def get(self, id):
        row = conn.get_row(id)
        d = {}

        # this is absolute garbage...
        # why on earth is there not any easier way to
        # serialize a SQL Alchemy query?
        for k, v in row.pop().__dict__.items():
            if k[0] != '_':
                d[k] = v
        return d, 201
