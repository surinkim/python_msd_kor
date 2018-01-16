# Chapter02
# flask_error.py
from flask import Flask, jsonify, abort
from werkzeug.exceptions import HTTPException, default_exceptions, _aborter

def JsonApp(app):
    def error_handling(error):
        if isinstance(error, HTTPException):
            result = {'code': error.code, 'description': error.description,
                        'message': str(error.code) +" " + error.name}
        else:
            description = _aborter.mapping[500].description
            result = {'code': 500, 'description': description,
                        'message': str(error)}
        resp = jsonify(result)
        resp.status_code = result['code']
        return resp

    for code in default_exceptions.keys():
        app.register_error_handler(code, error_handling)
    return app

app = JsonApp(Flask(__name__))

@app.route('/api')
def my_microservice():
    raise TypeError("Some Exception")

if __name__ == '__main__':
    app.run()
