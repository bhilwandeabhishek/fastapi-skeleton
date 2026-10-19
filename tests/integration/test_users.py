import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from src.database import get_db
from src.main import app


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch):
    test_engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    test_session_local = sessionmaker(
        bind=test_engine,
        autoflush=False,
        expire_on_commit=False,
    )

    def override_get_db():
        with test_session_local() as db:
            yield db

    monkeypatch.setattr("src.main.engine", test_engine)
    app.dependency_overrides[get_db] = override_get_db
    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.pop(get_db, None)
        test_engine.dispose()


def test_user_crud_flow(client: TestClient) -> None:
    user_data = {
        "userName": "Ada Lovelace",
        "userEmail": "ada@example.com",
    }

    created = client.post("/api/v1/users", json=user_data)
    assert created.status_code == 201
    user = created.json()
    assert user == {
        "id": 1,
        "userName": "Ada Lovelace",
        "userEmail": "ada@example.com",
    }

    listed = client.get("/api/v1/users")
    assert listed.status_code == 200
    assert listed.json() == [user]

    fetched = client.get(f"/api/v1/users/{user['id']}")
    assert fetched.status_code == 200
    assert fetched.json() == user

    updated = client.put(
        f"/api/v1/users/{user['id']}",
        json={"userName": "Ada Byron", "userEmail": "ada.byron@example.com"},
    )
    assert updated.status_code == 200
    assert updated.json()["userName"] == "Ada Byron"

    deleted = client.delete(f"/api/v1/users/{user['id']}")
    assert deleted.status_code == 204
    assert client.get(f"/api/v1/users/{user['id']}").status_code == 404
    assert client.get("/api/v1/users").json() == []


def test_user_errors_use_shared_feedback_response(client: TestClient) -> None:
    missing = client.get("/api/v1/users/999")
    assert missing.status_code == 404
    assert missing.json()["error"]["code"] == "user_not_found"

    invalid = client.post(
        "/api/v1/users",
        json={"userName": "", "userEmail": "not-an-email"},
    )
    assert invalid.status_code == 422
    assert invalid.json()["error"]["code"] == "validation_error"
    assert invalid.json()["error"]["details"]

    user_data = {"userName": "Grace Hopper", "userEmail": "grace@example.com"}
    assert client.post("/api/v1/users", json=user_data).status_code == 201
    duplicate = client.post("/api/v1/users", json=user_data)
    assert duplicate.status_code == 409
    assert duplicate.json()["error"]["code"] == "user_conflict"
