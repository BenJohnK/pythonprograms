x=int(input("input no. to check whether it is prime"))
k=x//2
check=False
for i in range(2,k+1):
    if x % i == 0:
        check=True
        break
if check == True:
    print("Given no. is not prime")
else:
    print("Given no. is prime")