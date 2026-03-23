import pytest
from src.auth.auth import get_password_hash
from src.db.models import User

test_data = {
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "email": "john.doe@test.com",
    "password": "testpass456"
}

def test_register_user(test_client, test_db_session):
    response = test_client.post("/users/me/register", json=test_data)

    assert response.json()["status"] == 201
    assert response.json()["data"]["username"] == test_data["username"]
    assert response.json()["data"]["email"] == test_data["email"]

def test_login_user(test_client, test_db_session):
    test_db_session.add(User(**test_data, password_hash=get_password_hash(test_data["password"])))
    test_db_session.commit()

    response = test_client.post("/users/me/login", json={
        "username": test_data["username"],
        "password": test_data["password"]
    })

    assert response.json()["status"] == 201
    assert response.json()["data"]["username"] == test_data["username"]
    assert response.json()["data"]["email"] == test_data["email"]

def test_get_info_current_user(test_client, test_db_session):
    test_db_session.add(User(**test_data, password_hash=get_password_hash(test_data["password"])))
    test_db_session.commit()

    login_response = test_client.post("/users/me/login", json={
        "username": test_data["username"],
        "password": test_data["password"]
    })

    token = login_response.json()["data"]["access_token"]

    response = test_client.get("/users/me/", headers={"Authorization": f"Bearer {token}"})
    
    assert response.json()["status"] == 200
    assert response.json()["data"]["username"] == test_data["username"]
    assert response.json()["data"]["email"] == test_data["email"]

def test_reset_password_user(test_client, test_db_session):
    test_db_session.add(User(**test_data, password_hash=get_password_hash(test_data["password"] + "haha")))
    test_db_session.commit()

    response = test_client.post("/users/me/password", json={
        "username": test_data["username"],
        "password": test_data["password"]
    })

    assert response.json()["status"] == 201
    assert response.json()["data"]["username"] == test_data["username"]
    assert response.json()["data"]["email"] == test_data["email"]
    assert response.json()["data"]["password"] == test_data["password"]
