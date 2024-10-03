import json
import unittest

from sqlalchemy import text

from app import create_app, db
from app.tests.basetest import BaseTestCase


class CreateUserApiTestCase(BaseTestCase):

    def test_create_user_valid(self):
        response = self.client.post('/api/users', json={
            'username': 'validuser',
            'email': 'validuser@example.com',
            'password': 'password123'
        })
        assert response.status_code == 201

    def test_create_user_invalid_email_format(self):
        response = self.client.post('/api/users', json={
            'username': 'validuser',
            'email': 'invalid-email',
            'password': 'password123'
        })
        assert response.status_code == 400
        assert b'Invalid email' in response.data

    def test_create_user_username_too_short(self):
        response = self.client.post('/api/users', json={
            'username': 'usr',
            'email': 'validuser@example.com',
            'password': 'password123'
        })
        assert response.status_code == 400
        assert b'Username must be between 5 and 50 characters' in response.data

    def test_create_user_username_too_long(self):
        response = self.client.post('/api/users', json={
            'username': 'a' * 51,
            'email': 'validuser@example.com',
            'password': 'password123'
        })
        assert response.status_code == 400
        assert b'Username must be between 5 and 50 characters' in response.data

    def test_create_user_email_not_unique(self):
        with self.app.app_context():
            db.session.execute(text("INSERT INTO user (username, email, password) VALUES ('existinguser', 'existing@example.com', 'password123')"))
            db.session.commit()

        response = self.client.post('/api/users', json={
            'username': 'newuser',
            'email': 'existing@example.com',
            'password': 'password123'
        })
        assert response.status_code == 400
        assert b'Email already exists' in response.data


if __name__ == '__main__':
    unittest.main()