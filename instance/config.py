

db_config = {
    'user': 'kmacneneyjr',
    'pw': '',
    'db': 'nyc_air',
    'host': 'localhost',
    'port': '5432',
}


def generate_sql_url(config):
    url = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s'
    return url % config
