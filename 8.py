t=tuple()
n=int(input("Total number of values in tuple"))
for i in range(n):
    a=input("enter elements")
    t=t+(a,)
print ("minimum value at =",t.index(min(t)))