import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"WeatherApp" in response.data

def test_get_weather(client):
    response = client.post('/weather', data={'location': 'London'})
    assert response.status_code == 200
    assert b"London" in response.data
