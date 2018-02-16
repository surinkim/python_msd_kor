from flask import Flask, jsonify
from flakon import crossdomain

app = Flask(__name__)




@app.route('/api/runs.json')
@crossdomain()
def _runs():
    run1 = {'title': 'Endurance', 'type': 'training'}
    run2 = {'title': '10K de chalon', 'type': 'race'}
    _data = [run1, run2]
    return jsonify(_data)

if __name__ == '__main__':
    app.run(port=5002)
