import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config.update(TESTING=True)
    with flask_app.test_client() as client:
        yield client


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_list_tasks_returns_seed_data(client):
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert len(resp.get_json()) >= 2


def test_create_task(client):
    resp = client.post("/tasks", json={"title": "Write tests"})
    assert resp.status_code == 201
    body = resp.get_json()
    assert body["title"] == "Write tests"
    assert body["done"] is False


def test_create_task_without_title_fails(client):
    resp = client.post("/tasks", json={})
    assert resp.status_code == 400


def test_get_missing_task_returns_404(client):
    resp = client.get("/tasks/999999")
    assert resp.status_code == 404
