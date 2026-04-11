from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/weather")
def weather():
    data = {"city": "Nagpur", "temp": 32}
    return jsonify(data)