import pytest
from app import app

@pytest.fixture()
def app():
    app = app()
    app.config.update({
        "TESTING": True,
        })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, test!' in response.data
