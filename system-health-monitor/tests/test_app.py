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

def test_index_loads(client):
    resp = client.get("/")
    assert resp.status_code == 200

def test_stats_returns_json(client):
    resp = client.get("/api/stats")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "cpu" in data
    assert "ram" in data
    assert "disk" in data
    assert "network" in data
    assert "processes" in data
