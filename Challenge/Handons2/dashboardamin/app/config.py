import os

# basedir = os.path.abspath(os.path.dirname(__file__))
# db_path = os.path.join(basedir, 'shopee.db')

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shopee.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False