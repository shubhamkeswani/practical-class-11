my_text = str(input("Enter your text: ")).lower()
my_clean_text = my_text.replace(" ","").replace("!","")
print("Original text: {}".format(my_text))
my_dict={}
for i in my_clean_text:
    my_dict[i]=my_dict.get(i,0)+1
print("\nFrequency of characters:")
for j in sorted(my_dict, key=my_dict.get, reverse=True):
    print(j+":",my_dict[j],"time(s)")