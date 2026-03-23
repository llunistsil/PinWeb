import os
from dotenv import load_dotenv
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.exc import OperationalError as SQLAlchemyOperationalError  
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, Session

from src.db.models import User, Priority, Task, ScheduleTask, TimeEntry, Schedule, Notification
from src.main import app
from src.db.connection import get_session

load_dotenv()
test_db_url = os.getenv('DB_TEST')

@pytest.hookimpl(tryfirst=True)  
def pytest_sessionstart(session):
    try:  
        engine = create_engine(  
            test_db_url,  
            poolclass=StaticPool,  
        )  
        connection = engine.connect()  
        connection.close()
        print("Database connection successful........")
    except SQLAlchemyOperationalError as e:  
        print(f"Failed to connect to the database at {test_db_url}: {e}")  
        pytest.exit(  
            "Stopping tests because database connection could not be established."  
        )

@pytest.fixture(scope="session")
def test_db_engine():
    engine = create_engine(test_db_url)
    SQLModel.metadata.create_all(engine)
    yield engine
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def test_db_session(test_db_engine):
    test_db_engine = create_engine(  
        test_db_url,  
        poolclass=StaticPool,  
    )  
    connection = test_db_engine.connect()  
    transaction = connection.begin()  

    with Session(bind=connection) as session:
        yield session

    transaction.rollback()  
    connection.close()

@pytest.fixture(scope="function")
def test_client(test_db_session):
    def override_get_db():  
        try:  
            yield test_db_session  
        finally:  
            test_db_session.close()

    app.dependency_overrides[get_session] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
