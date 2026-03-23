import pytest
from src.db.models import Priority, Task, User

def test_create_task(test_client, test_db_session):
    user_id = 1
    priority_id = 1
    test_db_session.add_all([
        User(id=user_id, username="task_owner", email="owner@tasks.local"),
        Priority(id=priority_id, name="Critical")
    ])
    test_db_session.commit()
    response = test_client.post("/tasks", json={
        "user_id": user_id,
        "priority_id": priority_id,
        "description": "Sample task description",
        "deadline": "2024-06-30T18:00:00"
    })

    assert response.json()["status"] == 201
    assert response.json()["data"]["user_id"] == user_id
    assert response.json()["data"]["priority_id"] == priority_id
    assert response.json()["data"]["description"] == "Sample task description"
    assert response.json()["data"]["deadline"] == "2024-06-30T18:00:00"

def test_get_tasks(test_client, test_db_session):
    user_id = 1
    priority_id = 1
    test_db_session.add_all([
        User(id=user_id, username="task_owner", email="owner@tasks.local"),
        Priority(id=priority_id, name="Critical")
    ])
    test_db_session.commit()
    test_db_session.add_all([
        Task(user_id=user_id, priority_id=priority_id, description="First task item", deadline="2024-06-30T18:00:00"),
        Task(user_id=user_id, priority_id=priority_id, description="Second task item", deadline="2024-07-15T12:00:00")
    ])
    test_db_session.commit()

    response = test_client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0]["description"] == "First task item"
    assert response.json()[1]["description"] == "Second task item"

def test_get_task(test_client, test_db_session):
    user_id = 1
    priority_id = 1
    test_db_session.add_all([
        User(id=user_id, username="task_owner", email="owner@tasks.local"),
        Priority(id=priority_id, name="Critical")
    ])
    test_db_session.commit()
    task_id = 1
    test_db_session.add(Task(id=task_id, user_id=user_id, priority_id=priority_id, description="Sample task description", deadline="2024-06-30T18:00:00"))
    test_db_session.commit()

    response = test_client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["user_id"] == user_id
    assert response.json()["priority_id"] == priority_id
    assert response.json()["description"] == "Sample task description"
    assert response.json()["deadline"] == "2024-06-30T18:00:00"

def test_update_task(test_client, test_db_session):
    user_id = 1
    priority_id = 1
    test_db_session.add_all([
        User(id=user_id, username="task_owner", email="owner@tasks.local"),
        User(id=user_id + 1, username="another_user", email="another@tasks.local"),
        Priority(id=priority_id, name="Critical"),
        Priority(id=priority_id + 1, name="Optional")
    ])
    task_id = 1
    test_db_session.add(Task(id=task_id, user_id=user_id + 1, priority_id=priority_id + 1, description="Original task text", deadline="2024-01-15T10:00:00"))
    test_db_session.commit()

    response = test_client.patch(f"/tasks/{task_id}", json={
        "user_id": user_id,
        "priority_id": priority_id,
        "description": "Modified task text",
        "deadline": "2025-03-20T14:30:00"
    })

    assert response.status_code == 200
    assert response.json()["user_id"] == user_id
    assert response.json()["priority_id"] == priority_id
    assert response.json()["description"] == "Modified task text"
    assert response.json()["deadline"] == "2025-03-20T14:30:00"

def test_delete_task(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Task to remove", deadline="2024-06-30T18:00:00"))
    test_db_session.commit()

    response = test_client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["ok"] == True
