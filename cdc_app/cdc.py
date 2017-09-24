from flask_restful import Resource

from cdc_app.models import CdcChronicRaw

conn = CdcChronicRaw()


class CDCSummary(Resource):

    def __init__(self):
        super(CDCSummary, self).__init__()

    @staticmethod
    def get():
        cols = conn.get_table_summary()
        response = {
            "count": conn.query.count(),
            "columns": [
                col for col in cols
            ]
        }
        return response, 201

