from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/status")
def status():
    return jsonify({
        "status": "ok",
        "server_time": datetime.now().isoformat()
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
