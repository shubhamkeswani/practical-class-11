lst=eval(input('Enter list:'))
length=len(lst)
element=int(input('Enter element to be searched for:'))
for i in range(0,length):
  if element==lst[i]:
        print(element,'found at index',i)
        break
if i == length-1:
  print(element,'not found in given list')