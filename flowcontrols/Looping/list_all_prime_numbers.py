low=int(input("Enter lower limit"))
up=int(input("Enter upper limit"))
for i in range(low,up+1):
    check=False
    k=i//2
    for j in range(2,k):
        if i % j == 0:
            check=True
            break
    if check == False:
        print(i, end=" ")


