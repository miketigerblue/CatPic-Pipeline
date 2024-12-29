
# app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    # fetch random cat pic from an API
    response = requests.get("https://api.thecatapi.com/v1/images/search").json()
    cat_url = response[0]['url']
    return f"<h1>Random Cat Picture!</h1><img src='{cat_url}' alt='cat'/>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
