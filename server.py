# server.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "✅ Mobile Diagnosis Tool API is running"})

@app.route("/device")
def device():
    # Placeholder: hapa baadaye tutaunganisha na modules/device_info.py
    return jsonify({
        "brand": "Unknown",
        "model": "Unknown",
        "os": "Unknown",
        "battery": "Unknown"
    })
