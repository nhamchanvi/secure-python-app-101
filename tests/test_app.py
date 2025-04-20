# tests/test_app.py
import pytest
from app import app as flask_app # Import the Flask app instance

@pytest.fixture()
def app():
  """Create a test app instance."""
  flask_app.config.update({
      "TESTING": True,
  })
  # You can add other configurations for testing if needed
  yield flask_app

@pytest.fixture()
def client(app):
  """Create a test client using the app fixture."""
  return app.test_client()

# --- Test Functions ---

def test_home_page(client):
  """Test the homepage route."""
  response = client.get('/')
  assert response.status_code == 200
  assert b"Welcome to the Simple Web App!" in response.data

def test_hello_default(client):
  """Test the /hello route without a name."""
  response = client.get('/hello')
  assert response.status_code == 200
  assert b"Hello, World!" in response.data

def test_hello_with_name(client):
  """Test the /hello route with a name parameter."""
  response = client.get('/hello?name=DevSecOps')
  assert response.status_code == 200
  assert b"Hello, DevSecOps!" in response.data

def test_hello_sanitization(client):
  """Test basic input sanitization on /hello."""
  response = client.get('/hello?name=<script>alert("xss")</script>')
  assert response.status_code == 200
  assert b"<script>" not in response.data # Check that '<' was escaped
  assert b'Hello, &lt;script&gt;alert("xss")&lt;/script&gt;!' in response.data

def test_api_status(client):
    """Test the API status endpoint."""
    response = client.get('/api/status')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "OK"
    assert json_data["service"] == "Simple Web App"