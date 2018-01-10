from flask import make_response, Flask
from urllib.parse import urlparse

app = Flask(__name__)

# domain:port
SAFE_DOMAINS = ['github.com:443', 'ziade.org:443']

@app.after_request
def check_redirect(response):
    if response.status_code != 302:
        return response
    url = urlparse(response.location)
    netloc = url.netloc
    if url.scheme == 'http' and not netloc.endswith(':80'):
        netloc += ':80'
    if url.scheme == 'https' and not netloc.endswith(':443'):
        netloc += ':443'
    if netloc not in SAFE_DOMAINS:
        # not using abort() here or it'll break the hook
        return make_response('Forbidden', 403)
    return response