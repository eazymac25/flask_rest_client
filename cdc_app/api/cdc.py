from flask_restful import Resource, reqparse

from cdc_app.model.cdc_chronic_raw import CdcChronicRaw
from cdc_app.api.utils import jsoncast

conn = CdcChronicRaw()


class CDCSummary(Resource):

    def __init__(self):
        super(CDCSummary, self).__init__()

    @staticmethod
    def get():
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

    @staticmethod
    @jsoncast('dict')
    def get(record_id):

        row = conn.get_row(record_id)
        if row:
            return row.pop(), 201
        else:
            return {"error": "No record with id %s" % record_id}, 404


class CDCRecords(Resource):

    def __init__(self):
        super(CDCRecords, self).__init__()

    @staticmethod
    @jsoncast('list')
    def get(start, stop):
        """
        yeah you guessed it... pagenation

        :param start: start int for query
        :param stop: stop in for query
        :return: list of records
        """
        print(start, stop)
        rows = conn.get_over_range(start, stop)
        print(rows)
        return rows, 201
