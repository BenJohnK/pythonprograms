lst = []
list_length=int(input("Enter length of list"))
f = 0
for i in range(list_length):
    ele = int(input("Enter element"))
    lst.append(ele)
k = int(input("Enter number to search"))

f = 0

up = list_length-1
while up > 0:
    low = 0
    while low != up:
        if lst[low]+lst[up] == k:
            print(lst[low], lst[up])
            f = 1
        low = low+1
    up=up-1
if f == 0:
    print("no pair found")

