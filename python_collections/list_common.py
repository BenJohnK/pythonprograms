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
j=0
i=0
lst.sort()
lst2.sort()
while i<list_length:
    if lst[i]>lst2[j]:
        j=j+1
    elif lst[i]<lst2[j]:
        i=i+1
    else:
        lst3.append(lst[i])
        i=i+1
        j=j+1

print(lst3)


