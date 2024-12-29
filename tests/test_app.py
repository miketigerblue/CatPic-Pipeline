import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    rv = client.get("/")
    assert rv.status_code == 200
