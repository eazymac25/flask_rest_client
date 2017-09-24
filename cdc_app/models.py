from cdc_app import db


class CdcChronicRaw(db.Model):

    __tablename__ = 'cdc_chronic_raw'

    id = db.Column(db.Integer, primary_key=True)
    yearstart = db.Column(db.Text)
    yearend = db.Column(db.Text)
    locationabbr = db.Column(db.Text)
    locationdesc = db.Column(db.Text)
    datasource = db.Column(db.Text)
    topic = db.Column(db.Text)
    question = db.Column(db.Text)
    response = db.Column(db.Text)
    datavalueunit = db.Column(db.Text)
    datavaluetype = db.Column(db.Text)
    datavalue = db.Column(db.Text)
    datavaluealt = db.Column(db.Text)
    datavaluefootnotesymbol = db.Column(db.Text)
    datavaluefootnote = db.Column(db.Text)
    lowconfidencelimit = db.Column(db.Text)
    highconfidencelimit = db.Column(db.Text)
    stratificationcategory1 = db.Column(db.Text)
    stratification1 = db.Column(db.Text)
    stratificationcategory2 = db.Column(db.Text)
    stratification2 = db.Column(db.Text)
    stratificationcategory3 = db.Column(db.Text)
    stratification3 = db.Column(db.Text)
    geolocation = db.Column(db.Text)
    responseid = db.Column(db.Text)
    locationid = db.Column(db.Text)
    topicid = db.Column(db.Text)
    questionid = db.Column(db.Text)
    datavaluetypeid = db.Column(db.Text)
    stratificationcategoryid1 = db.Column(db.Text)
    stratificationid1 = db.Column(db.Text)
    stratificationcategoryid2 = db.Column(db.Text)
    stratificationid2 = db.Column(db.Text)
    stratificationcategoryid3 = db.Column(db.Text)
    stratificationid3 = db.Column(db.Text)
    
    def __init__(self):
        super(CdcChronicRaw, self).__init__()

    def get_table_summary(self):
        """
        get the table column names
        :return: list of column names
        """
        return self.__table__.columns.keys()

    def get_count(self):
        self.query.count()
