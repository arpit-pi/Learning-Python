def func(*args):
    for i in range(0,len(args)):
        print(args[i])

my_list=[1,2,3,4]

func(*range(2,10))
