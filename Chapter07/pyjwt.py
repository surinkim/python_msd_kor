# Chapter07
# pyjwt.py
import jwt

def create_token(alg='HS256', secret='secret', **data):
    return jwt.encode(data, secret, algorithm=alg)

def read_token(token, secret='secret', algs=['HS256']):
    return jwt.decode(token, secret, algorithms=algs)

token = create_token(some='data', inthe='token')
print(token)
read = read_token(token)
print(read)