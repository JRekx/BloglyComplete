from post2 import app

# Fixture for test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

# Test cases for post.py
def test_posts_index(client):
    response = client.get('/posts')
    assert response.status_code == 200

def test_posts_new_form(client):
    response = client.get('/posts/new')
    assert response.status_code == 200

def test_posts_new(client):
    response = client.post('/posts/new', data={'title': 'Test Post', 'content': 'This is a test post content'})
    assert response.status_code == 302  # Redirect after adding a new post