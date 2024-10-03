import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import User
from app.database import get_db, Base, engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_user(client, db):
    response = client.post(
        "/users/",
        json={"username": "testuser", "email": "testuser@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "testuser@example.com"
    user = db.query(User).filter(User.email == "testuser@example.com").first()
    assert user is not None

def test_create_user_existing_email(client, db):
    user = User(username="existinguser", email="existing@example.com", password="password123")
    db.add(user)
    db.commit()
    response = client.post(
        "/users/",
        json={"username": "newuser", "email": "existing@example.com", "password": "password123"}
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Email already registered"

def test_create_user_invalid_email(client):
    response = client.post(
        "/users/",
        json={"username": "invalidemailuser", "email": "invalid-email", "password": "password123"}
    )
    assert response.status_code == 422

def test_create_user_short_password(client):
    response = client.post(
        "/users/",
        json={"username": "shortpassworduser", "email": "shortpassword@example.com", "password": "short"}
    )
    assert response.status_code == 422

    def test_create_user_short_username(client):
        response = client.post(
            "/users/",
            json={"username": "short", "email": "shortusername@example.com", "password": "password123"}
        )
        assert response.status_code == 422

    def test_create_user_long_username(client):
        response = client.post(
            "/users/",
            json={"username": "averylongusername", "email": "longusername@example.com", "password": "password123"}
        )
        assert response.status_code == 422

    def test_create_user_valid_username(client):
        response = client.post(
            "/users/",
            json={"username": "validname", "email": "validname@example.com", "password": "password123"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "validname"
        assert data["email"] == "validname@example.com"
