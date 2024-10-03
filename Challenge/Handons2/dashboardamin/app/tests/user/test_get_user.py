import json
import unittest

from sqlalchemy import text

from app import create_app, db


class UsersListApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_all_users(self):
        # Insert test data into the database
        # not use Alchemy model
        with self.app.app_context():
            db.session.execute(text("INSERT INTO user (username, email, password) VALUES ('John Doe', 'jonedoe@ex.com', 'password123')"))
            db.session.execute(text("INSERT INTO user (username, email, password) VALUES ('Jane Doe', 'janedoe@ex.com', 'password123')"))
            db.session.commit()

            response = self.client.get("/api/users")
            assert response.status_code == 200

            # assert in response data there are 2 users
            list_users = json.loads(response.text)
            assert len(list_users) == 2


if __name__ == '__main__':
    unittest.main()