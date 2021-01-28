x = int(input("Enter number 1"))
y = int(input("Enter number 2"))
z = int(input("Enter number 3"))
list = [x, y, z]
list.sort()
# for x in list:
#     print(x, end="<")
l = len(list)
print(l)
for i in range(l):
    if i != (l-1):
        print(list[i], end="<")
    else:
        print(list[i])
