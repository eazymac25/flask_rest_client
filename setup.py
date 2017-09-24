from setuptools import setup, find_packages


setup(
    name='rest_clinet',
    version='1.0.0',
    author='Kyle MacNeney',
    packages=find_packages(),
    install_requires=[
        'flask',
        'psycopg2',
        'flask-restful',
        'flask-sqlalchemy',
    ]
)
