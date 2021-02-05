lst = []
list_length=int(input("Enter length of list"))
f = 0
for i in range(list_length):
    ele = int(input("Enter element"))
    lst.append(ele)
k = int(input("Enter number to pair search"))
lst.sort()
flag=0
low=0
up=list_length-1
while low!=up:
    if k > lst[low]+lst[up]:
        low = low+1
    elif k < (lst[low] + lst[up]):
        up = up - 1
    else:
        print(lst[low], lst[up])
        flag=1
        break

if flag == 0:
    print("No pair found")