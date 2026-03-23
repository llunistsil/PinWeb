import pytest
from src.db.models import Task, TimeEntry

def test_create_time_entry(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Work task", deadline="2024-06-30T18:00:00"))
    test_db_session.commit()
    response = test_client.post("/time_entries", json={
        "task_id": task_id,
        "start_time": "2024-05-01T09:00:00",
        "end_time": "2024-05-01T17:00:00",
        "duration": 120
    })

    assert response.json()["status"] == 201
    assert response.json()["data"]["task_id"] == task_id
    assert response.json()["data"]["start_time"] == "2024-05-01T09:00:00"
    assert response.json()["data"]["end_time"] == "2024-05-01T17:00:00"
    assert response.json()["data"]["duration"] == 120

def test_get_time_entries(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Work task", deadline="2024-06-30T18:00:00"))
    test_db_session.commit()
    test_db_session.add_all([
        TimeEntry(id=1, task_id=task_id, start_time="2024-05-01T09:00:00", end_time="2024-05-01T17:00:00", duration=120),
        TimeEntry(id=2, task_id=task_id, start_time="2024-05-02T09:00:00", end_time="2024-05-02T17:00:00", duration=120)
    ])
    test_db_session.commit()

    response = test_client.get("/time_entries")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0]["id"] == 1
    assert response.json()[1]["id"] == 2

def test_get_time_entry(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Work task", deadline="2024-06-30T18:00:00"))
    test_db_session.commit()
    time_entry_id = 1
    test_db_session.add(TimeEntry(id=time_entry_id, task_id=task_id, start_time="2024-05-01T09:00:00", end_time="2024-05-01T17:00:00", duration=120))
    test_db_session.commit()

    response = test_client.get(f"/time_entries/{time_entry_id}")

    assert response.status_code == 200
    assert response.json()["task_id"] == task_id
    assert response.json()["start_time"] == "2024-05-01T09:00:00"
    assert response.json()["end_time"] == "2024-05-01T17:00:00"
    assert response.json()["duration"] == 120

def test_update_time_entry(test_client, test_db_session):
    task_id = 1
    test_db_session.add_all([
        Task(id=task_id, description="Work task", deadline="2024-06-30T18:00:00"),
        Task(id=task_id + 1, description="Another task", deadline="2024-07-15T12:00:00")
    ])
    test_db_session.commit()
    time_entry_id = 1
    test_db_session.add(TimeEntry(id=time_entry_id, task_id=task_id + 1, start_time="2024-05-01T09:00:00", end_time="2024-05-01T17:00:00", duration=120))
    test_db_session.commit()

    response = test_client.patch(f"/time_entries/{time_entry_id}", json={
        "task_id": task_id,
        "start_time": "2024-05-02T10:00:00",
        "end_time": "2024-05-02T18:00:00",
        "duration": 60
    })

    assert response.status_code == 200
    assert response.json()["task_id"] == task_id
    assert response.json()["start_time"] == "2024-05-02T10:00:00"
    assert response.json()["end_time"] == "2024-05-02T18:00:00"
    assert response.json()["duration"] == 60

def test_delete_time_entry(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Work task", deadline="2024-06-30T18:00:00"))
    test_db_session.commit()
    time_entry_id = 1
    test_db_session.add(TimeEntry(id=time_entry_id, task_id=task_id, start_time="2024-05-01T09:00:00", end_time="2024-05-01T17:00:00", duration=120))
    test_db_session.commit()

    response = test_client.delete(f"/time_entries/{time_entry_id}")

    assert response.status_code == 200
    assert response.json()["ok"] == True
