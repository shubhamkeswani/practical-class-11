n = int(input("Enter the number of students: "))
list1 = []
for i in range(n):
    name = input()
    list1.append(name)
tuple1 = tuple(list1)
findName = input("Enter name to find: ")
def userDefinedSearch():
    for item in tuple1:
        if item==findName:
            print("Name found")
            return
    print("Name not found")
userDefinedSearch()
