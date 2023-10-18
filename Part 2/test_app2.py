from app2 import app

# Fixture for test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

# Test cases for app.py
def test_homepage_redirects(client):
    response = client.get('/')
    assert response.status_code == 302
    assert response.location == 'http://localhost/users'

