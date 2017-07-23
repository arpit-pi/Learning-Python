from functools import *

def add(a,b,c):
    return a+b+c

onlya=partial(add,b=10,c=20)

print(onlya(10))
    
