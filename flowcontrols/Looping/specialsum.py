x = int(input("Enter number"))
sum = 0
specialnumber = x
for i in range(x):
    sum = sum+specialnumber
    specialnumber = (specialnumber*10)+x

print(sum)

