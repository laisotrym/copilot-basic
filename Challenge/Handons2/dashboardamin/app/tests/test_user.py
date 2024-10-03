import unittest
from app import create_app, db
from app.user.model import User


class UsersApiTestCase(unittest.TestCase):
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

    def test_create_user(self):
        response = self.client.post('/api/users', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 201)

        response_data = response.get_json()
        self.assertIn('id', response_data)

    def test_get_all_users(self):
        # insert 2 users into the database
        user1 = User(username='testuser1', email='test1@example.com', password='password')
        user2 = User(username='testuser2', email='test2@example.com', password='password')
        with self.app.app_context():
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()

            response = self.client.get('/api/users')
            self.assertEqual(response.status_code, 200)

            # assert in response data there are 2 users
            response_data = response.get_json()
            self.assertEqual(len(response_data), 2)

    def test_get_user(self):
        user = User(username='testuser', email='test@example.com', password='password')
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()

            response = self.client.get(f'/api/users/{user.id}')
            self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        user = User(username='testuser', email='test@example.com', password='password')
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()

            response = self.client.put(f'/api/users/{user.id}', json={
                'username': 'updateduser',
                'email': 'updated@example.com',
                'password': 'newpassword'
            })
            self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        user = User(username='testuser', email='test@example.com', password='password')
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()

            response = self.client.delete(f'/api/users/{user.id}')
            self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()
