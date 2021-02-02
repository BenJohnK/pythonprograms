
lst=[]
list_length=int(input("Enter list length"))
for i in range(list_length):
    x=int(input("Enter element"))
    lst.append(x)
print(lst)

list2=[]
for i in range(list_length):
    sum=0
    for j in range(list_length):
        if i!=j:
            sum=sum+lst[j]
    list2.append(sum)

print(list2)

