a,b=10,20

min=a if a<b else b
print(min)
print((b,a)[a<b])  #using Tuple
print({True:a,False:b}[a<b])

print((lambda:b,lambda:a)[a<b]())
