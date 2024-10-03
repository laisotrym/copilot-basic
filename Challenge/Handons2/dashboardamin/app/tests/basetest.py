import unittest
from app import create_app, db


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        config = {
            'TESTING': True,
            # 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///shopeetest.db'
        }
        self.app = create_app(config)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
