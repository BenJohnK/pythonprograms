lst = []
lst2 = []
lst3 = []
list_length=int(input("Enter length of first list"))

for i in range(list_length):
    ele = int(input("Enter element"))
    lst.append(ele)
list_length2=int(input("Enter length of second list"))

for i in range(list_length2):
    ele = int(input("Enter element"))
    lst2.append(ele)

for i in range(0,list_length):
    for j in range(0,list_length2):
        if lst[i]==lst2[j]:
            lst3.append(lst[i])

print(lst3)


