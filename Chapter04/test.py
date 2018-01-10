from greenlet import greenlet
def test1(x, y):
    z = gr2.switch(x+y)
    print(z)
