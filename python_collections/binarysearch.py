lst = []
list_length = int(input("Enter length of list"))
flag = 0
for i in range(list_length):
    ele = int(input("Enter element"))
    lst.append(ele)
lst.sort()
k = int(input("Enter number to search"))
low=0
up=list_length-1
mid=(low+up)//2

def binarysearch(low,mid,up):
    if k > lst[mid]:
        low = mid + 1
        mid=(low+up)//2
        binarysearch(low,mid,up)
    elif k < lst[mid]:
        up= mid - 1
        mid=(low+up)//2
        binarysearch(low,mid,up)
    elif k == lst[mid]:
        flag = 1

binarysearch(low,mid,up)

if (flag == 1):
    print("Element found0")
else:
    print("Not found")

