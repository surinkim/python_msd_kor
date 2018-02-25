# Chapter01
# gevent_example.py
from gevent import monkey; monkey.patch_all()

def application(environ, start_response):
    headers = [('Content-type', 'application/json')]
    start_response('200 OK', headers)
    # 소켓으로 필요한 작업을 한다.
    return result