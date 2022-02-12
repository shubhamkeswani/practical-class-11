lst1=eval(input("Enter List 1"))
lst2=eval(input("Enter List 2"))
mx1=max(lst1)
mx2=max(lst2)
if mx1>=mx2:
    print(mx1,"the maximum value in is in the list 1 at index ",lst1.index(mx1))
else:
    print(mx2,"the maximum value in is in the list 2 at index ",lst2.index(mx2))