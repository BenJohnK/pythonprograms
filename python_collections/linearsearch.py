
lst=[]
list_length=int(input("Enter lenght of list"))
f=0
for i in range(list_length):
    ele=int(input("Enter element"))
    lst.append(ele)
x=int(input("Enter number to search"))
for ele in lst:
    if x == ele:
        f=1
if f==1:
    print("Found")
else:
    print("Not found")

