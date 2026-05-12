from flask import Flask
import requests

app = Flask(__name__)

@app.route('/call-a')
def call_a():
    response = requests.get('http://service_a:5000/data')

    return {
        "service_b_received": response.json()
    }

app.run(host='0.0.0.0', port=5001)