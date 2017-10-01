from flask_restful import Resource

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
