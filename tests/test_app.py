import pytest

from app import create_app
from app.routes import PORTFOLIO


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_index_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
    assert PORTFOLIO["name"].encode() in response.data


def test_about_page(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About Me" in response.data


def test_projects_page(client):
    response = client.get("/projects")
    assert response.status_code == 200
    assert b"Projects" in response.data
    assert b"Task Manager API" in response.data


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
