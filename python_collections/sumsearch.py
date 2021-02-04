lst=[]
list_length=int(input("Enter lenght of list"))
f=0
list2=[]
for i in range(list_length):
    ele=int(input("Enter element"))
    lst.append(ele)
x=int(input("Enter number to search"))

k=int(input("Enter element"))

for i in range(list_length):
    sum=0
    for j in range(list_length):
        if i!=j:
            sum=lst[i]+lst[j]
            if sum==k:
                list2.append(lst[i])
                list2.append(lst[j])

print(list2)

