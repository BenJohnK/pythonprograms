def binary_search(arr, x):
    lower = 0
    high = len(arr) - 1
    mid = 0

    while lower <= high:

        mid = (high + lower) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            lower = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


n1=int(input("Enter no. of elements in list1"))
n2=int(input("Enter no. of elements in list2"))
list1=[]
list2=[]
low=0
if n1<n2 or n1==n2:
    print("Enter elements of list1")
    for i in range(0,n1):
        x=int(input("Enter element"))
        list1.append(x)
    print("Enter elements of list2")
    for i in range(0,n2):
        x=int(input("Enter element"))
        list2.append(x)
    up=n2-1
else:
    print("Enter elements of list1")
    for i in range(0,n1):
        x=int(input("Enter element"))
        list2.append(x)
    print("Enter elements of list2")
    for i in range(0,n2):
        x=int(input("Enter element"))
        list1.append(x)
    up=n1-1
list1.sort()
list2.sort()
list3=[]
for ele in list1:
    if ele<list2[low] or ele>list2[up]:
        continue
    elif ele==list2[low] or ele==list2[up]:
        list3.append(ele)
    else:
        res=binary_search(list2, ele)
        if res!=-1:
            list3.append(ele)

print(list3)




