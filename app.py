# app.py
from flask import Flask, request, jsonify
import html # Import the html module

app = Flask(__name__)

@app.route('/')
def home():
  """Serves the homepage."""
  return "<h1>Welcome to the Simple Web App!</h1><p>This is the homepage.</p>"

@app.route('/hello')
def hello():
  """Says hello, optionally using a name query parameter."""
  name = request.args.get('name', 'World')
  # Use html.escape for proper sanitization
  name = html.escape(name)
  return f"<h1>Hello, {name}!</h1>" # Use f-string formatting

@app.route('/api/status')
def api_status():
    """A simple API endpoint."""
    return jsonify({"status": "OK", "service": "Simple Web App"})

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)