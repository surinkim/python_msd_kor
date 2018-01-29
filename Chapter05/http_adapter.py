# Chapter05
# http_adapter.py
from requests.adapters import HTTPAdapter
from requests import Session

class HTTPTimeoutAdapter(HTTPAdapter):
    def __init__(self, *args, **kw):
        self.timeout = kw.pop('timeout', 30.)
        print('self.timeout = ', self.timeout)

        super().__init__(*args, **kw)

    def send(self, request, **kw):
        timeout = kw.get('timeout')
        if timeout is None:
            kw['timeout'] = self.timeout
        return super().send(request, **kw)

def setup_connector(app, name='default', **options):
    if not hasattr(app, 'extensions'):
        app.extensions = {}

    if 'connectors' not in app.extensions:
        app.extensions['connectors'] = {}
    session = Session()

    if 'auth' in options:
        session.auth = options['auth']

    headers = options.get('headers', {})

    if 'Content-Type' not in headers:
        headers['Content-Type'] = 'application/json'
    session.headers.update(headers)

    retries = options.get('retries', 3)
    #timeout은 아래 두 가지 중 하나의 방법으로 설정한다.
    #1)하나의 float 값으로 connect/read timeout 동일하게 설정.
    #2)하나의 float 튜플로 connect/read timeout을 다르게 설정.
    timeout = options.get('timeout', (5.0, 3.0)) #2)번 방법 사용

    adapter = HTTPTimeoutAdapter(max_retries=retries, timeout=timeout)
    session.mount('http://', adapter)
    app.extensions['connectors'][name] = session
    
    return session

def get_connector(app, name='default'):
    return app.extensions['connectors'][name]