#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n = int(input("Enter the no.of lines in the triangle"))
# lastlineno= 2*i-1
# spaceforfirst=lastlineno//2
spaceforfirst=n-1
for i in range(1,n+1):
    for k in range(0,spaceforfirst):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()
    spaceforfirst=spaceforfirst-1

spaceforfirst = 1
for i in range(n-1,0,-1):
    for k in range(0,spaceforfirst):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()
    spaceforfirst=spaceforfirst+1



