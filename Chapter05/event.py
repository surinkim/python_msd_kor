# Chapter05
# event.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/event', methods=['POST'])
def event_received():
    message = request.json['message']
    print('message = ', message)

    # 필요한 작업을 처리한다.
    # ...

    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run()