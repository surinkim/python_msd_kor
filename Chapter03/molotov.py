# Chapter03
# molotov.py
import json
from molotov import scenario

@scenario(5)
async def scenario_one(session):
    res = await session.get('http://localhost:5000/api').json()
    assert res['Hello'] == 'World!'

@scenario(30)
async def scenario_two(session):
     somedata = json.dumps({'OK': 1})
     res = await session.post('http://localhost:5000/api', data=somedata)
     assert res.status_code == 200
