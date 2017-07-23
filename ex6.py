def func(**kwargs):
    print(type(kwargs))
    for key in kwargs:
        print("%s = %s" %(key,kwargs[key]),end=" ;) ")

func(name="Flusha",team="fnatic",nick="Senor VAC")
