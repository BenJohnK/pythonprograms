x=int(input("Enter number 1"))
y=int(input("Enter number 2"))
if(int.__gt__(x,y)):
    print(x, "is greater than", y)
elif(int.__eq__(x,y)):
    print(x, "is equal to", y)
else:
    print(x, "is lesser than", y)