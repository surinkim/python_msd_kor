# Chapter02
# flask_variables_01.py
from flask import Flask, jsonify 
 
app = Flask(__name__) 
 
@app.route('/api/person/<person_id>')
def person(person_id):
    response = jsonify({'Hello': person_id})
    return response

if __name__ == '__main__': 
    app.run()


