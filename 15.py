details={}
def Recu():
    print("want to add press 1 and if you want phone number press 0 or press 2 to exit")
    t=int(input())
    if(t==1):
        n=1
        for i in range(0,n):
            name=input("Enter name")
            Phonenumber=int(input("Enter phone number"))
            details[name]=Phonenumber
            Recu()
    elif(t==0):
            f=input("Enter the person's name to get the phone number")
            x=details.get(f)
            print(x)
            Recu()
    else:exit()
Recu()