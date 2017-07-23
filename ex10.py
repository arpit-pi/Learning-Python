#Use of any and all

a,b,c,d,e=1,2,3,3,1

if any([a<b,b<e,a>e]):
    print("One of the conditions was true.")

if all([a<b,a==e,b<c]):
    print("All conditions are True.")
