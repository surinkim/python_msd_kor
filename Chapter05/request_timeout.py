# Chapter05
# request_timeout.py
from flask import Flask, jsonify 
from requests.exceptions import ReadTimeout
from flask_session import setup_connector, get_connector

app = Flask(__name__) 
setup_connector(app)

@app.route('/api', methods=['GET', 'POST'])
def my_microservice():
    with get_connector(app) as conn:
        try:
            result = conn.get('http://localhost:5000/api',timeout=2.0).json()
        except ReadTimeout:
            result = {}

    return jsonify({'result': result, 'Hello': 'World!'})

if __name__ == '__main__':
    app.run(port=5001)