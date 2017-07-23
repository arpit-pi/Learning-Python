a=1

def f():
    print('Inside f(): ',a)

def g():
    a=2
    print('Inside g(): ',a)

def h():
    global a
    print('Inside h():',a)
    a=10  #it's position affect the outcome of this function..

print('globally a=',a)
f()
g()
h()
