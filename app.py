from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load version from semver.txt if it exists
VERSION = "0.0.0"
try:
    with open('semver.txt', 'r') as f:
        VERSION = f.read().strip()
except FileNotFoundError:
    logger.warning("semver.txt not found, using default version")

@app.route('/')
def home():
    """Main page endpoint"""
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello World!</h1>
        <p>Version: {VERSION}</p>
        <p>This is a simple Flask application.</p>
    </body>
    </html>
    """

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': VERSION
    }), 200

@app.route('/ready')
def ready():
    """Readiness check endpoint"""
    return jsonify({
        'status': 'ready',
        'version': VERSION
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    logger.info(f'Starting Flask app on port {port}')
    app.run(host='0.0.0.0', port=port, debug=False)
