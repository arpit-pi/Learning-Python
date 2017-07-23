#PACKING AND UNPACKING

def unpack(a,b,c,d):
    print(a,b,c,d)

def pack(*args):     #packs multiple arguements into a tuple..
    args=list(args)  #to convert tuple into a list..

    args[1]='Book'
    args[2]='Air'
    unpack(*args)

pack('Mac','i','pro','lol')
