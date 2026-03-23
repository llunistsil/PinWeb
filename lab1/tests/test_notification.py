import pytest
from src.db.models import Notification, Task

def test_create_notification(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Sample task", deadline="2024-06-30T18:00:00"))
    test_db_session.commit()
    response = test_client.post("/notifications", json={
        "task_id": task_id,
        "message": "Reminder message",
        "sent_at": "2024-05-01T10:00:00Z"
    })

    assert response.json()["status"] == 201
    assert response.json()["data"]["task_id"] == task_id
    assert response.json()["data"]["message"] == "Reminder message"

def test_get_notifications(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Sample task", deadline="2024-06-30T18:00:00"))
    test_db_session.commit()
    test_db_session.add_all([
        Notification(task_id=task_id, message="First alert", sent_at="2024-05-01T10:00:00Z"),
        Notification(task_id=task_id, message="Second alert", sent_at="2024-05-02T11:00:00Z")
    ])
    test_db_session.commit()

    response = test_client.get("/notifications")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0]["message"] == "First alert"
    assert response.json()[1]["message"] == "Second alert"

def test_get_notification(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Sample task", deadline="2024-06-30T18:00:00"))
    test_db_session.commit()
    notification_id = 1
    test_db_session.add(Notification(id=notification_id, task_id=task_id, message="Reminder message", sent_at="2024-05-01T10:00:00Z"))
    test_db_session.commit()

    response = test_client.get(f"/notifications/{notification_id}")

    assert response.status_code == 200
    assert response.json()["task_id"] == task_id
    assert response.json()["message"] == "Reminder message"
    assert response.json()["sent_at"] == "2024-05-01T10:00:00"

def test_update_notification(test_client, test_db_session):
    task_id = 1
    test_db_session.add_all([
        Task(id=task_id, description="Sample task", deadline="2024-06-30T18:00:00"),
        Task(id=task_id + 1, description="Another task", deadline="2024-07-15T12:00:00")
    ])
    test_db_session.commit()
    notification_id = 1
    test_db_session.add(Notification(id=notification_id, task_id=task_id + 1, message="Original alert", sent_at="2024-05-01T10:00:00Z"))
    test_db_session.commit()

    response = test_client.patch(f"/notifications/{notification_id}", json={
        "task_id": task_id,
        "message": "Modified alert",
        "sent_at": "2024-05-10T14:00:00Z"
    })

    assert response.status_code == 200
    assert response.json()["task_id"] == task_id
    assert response.json()["message"] == "Modified alert"

def test_delete_notification(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Sample task", deadline="2024-06-30T18:00:00"))
    test_db_session.commit()
    notification_id = 1
    test_db_session.add(Notification(id=notification_id, task_id=task_id, message="Reminder message", sent_at="2024-05-01T10:00:00Z"))
    test_db_session.commit()

    response = test_client.delete(f"/notifications/{notification_id}")

    assert response.status_code == 200
    assert response.json()["ok"] == True
