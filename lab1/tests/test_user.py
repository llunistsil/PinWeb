import pytest
from src.db.models import User

def test_create_user(test_client, test_db_session):
    response = test_client.post("/users", json={
        "username": "demo_user",
        "email": "demo@test.local"
    })

    assert response.json()["status"] == 201
    assert response.json()["data"]["username"] == "demo_user"
    assert response.json()["data"]["email"] == "demo@test.local"


def test_get_users(test_client, test_db_session):
    test_db_session.add_all([
        User(username="alice_dev", email="alice@dev.local"),
        User(username="bob_dev", email="bob@dev.local")
    ])
    test_db_session.commit()

    response = test_client.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0]["username"] == "alice_dev"
    assert response.json()[1]["username"] == "bob_dev"

def test_get_user(test_client, test_db_session):
    user_id = 1
    test_db_session.add(User(id=user_id, username="demo_user", email="demo@test.local"))
    test_db_session.commit()

    response = test_client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["username"] == "demo_user"
    assert response.json()["email"] == "demo@test.local"

def test_update_user(test_client, test_db_session):
    user_id = 1
    test_db_session.add(User(id=user_id, username="demo_user", email="demo@test.local"))
    test_db_session.commit()

    response = test_client.patch(f"/users/{user_id}", json={
        "username": "modified_user",
        "email": "modified@test.local"
    })

    assert response.status_code == 200
    assert response.json()["username"] == "modified_user"
    assert response.json()["email"] == "modified@test.local"

def test_delete_user(test_client, test_db_session):
    user_id = 1
    test_db_session.add(User(id=user_id, username="demo_user", email="demo@test.local"))
    test_db_session.commit()

    response = test_client.delete(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["ok"] == True
