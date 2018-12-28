# Chapter05
# synchronouscalls.py
from requests import Session

s = Session()
s.headers['Content-Type'] = 'application/json'
s.auth = 'tarek', 'password'

# 호출이 일어날 때, 헤더와 인증 정보가 모두 설정된다.
s.get('http://localhost:5000/api').json()
s.get('http://localhost:5000/api2').json()
