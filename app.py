# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
  """Serves the homepage."""
  return "<h1>Welcome to the Simple Web App!</h1><p>This is the homepage.</p>"

@app.route('/hello')
def hello():
  """Says hello, optionally using a name query parameter."""
  name = request.args.get('name', 'World')
  # Basic input sanitization example (though minimal)
  name = name.replace('<', '&lt;').replace('>', '&gt;')
  return f"<h1>Hello, {name}!</h1>"

@app.route('/api/status')
def api_status():
    """A simple API endpoint."""
    return jsonify({"status": "OK", "service": "Simple Web App"})

# This is useful for running locally with `python app.py`
# For production/containers, a WSGI server like Gunicorn is better (see Dockerfile)
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)