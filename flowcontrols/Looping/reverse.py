number=input("Enter number") #123
x=(len(number))
num=int(number)
val=''
i=0
n1=0
while(i<x):
    n1=num%10
    val=val+str(n1)
    num=num//10
    i=i+1
print(val)
