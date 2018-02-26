# Chapter12
# sanic_1.py
from sanic import Sanic, response

app = Sanic(__name__)

@app.route("/api")
async def api(request):
    return response.json({'some': 'data'})

app.run()