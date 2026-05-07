from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "project": "Backend Hosting Test",
        "status": "Running Successfully",
        "developer": "Urwah Khalid",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": "Flask backend is live on server"
    })


@app.route("/api/info")
def info():
    return jsonify({
        "api_name": "Test API",
        "version": "1.0",
        "features": [
            "Flask Backend",
            "JSON Responses",
            "GitHub Integration",
            "Render Hosting"
        ]
    })


@app.route("/health")
def health():
    return jsonify({
        "health": "OK",
        "server": "Active"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)