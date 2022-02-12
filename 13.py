classxi=dict()
n=int(input("Enter total number of section in xi class: "))
i=1
while i<=n:
     a=input("Enter Section: ")
     b=input ("Enter stream name: ")
     classxi[i]=b
     i=i+1
print ("Class",'\t''Section''\t''Stream name')
for i in classxi:
     print ("XI",'\t',i,'\t',classxi[i])