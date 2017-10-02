from cdc_app.core import db


class BaseModel(db.Model):

    __abstract__ = True

    def __init__(self):
        super(BaseModel, self).__init__()

    def to_dict(self):
        pass
