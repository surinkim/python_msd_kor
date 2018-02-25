# Chapter12
# terminal_sample.py
def terminal():
    while True:
        msg = yield # msg에는 send() 호출로 보낸 값이 들어있다.
        if msg == 'exit':
            print("Bye!")
            break
        elif msg.startswith('echo'):
            print(msg.split('echo ', 1)[1])
        elif msg.startswith('eval'):
            print(eval(msg.split('eval', 1)[1]))