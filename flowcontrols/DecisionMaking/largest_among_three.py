number1=int(input("Enter number 1"))
number2=int(input("Enter number 2"))
number3=int(input("Enter number 3"))
if number1.__gt__(number2):
    temp = number1
    f=0
else:
    temp = number2
    f=1
if temp.__gt__(number3):
    print(temp,  "is the greatest")
    if f == 0:
        if number2.__gt__(number3):
            print(number2, "is second largest")
        else:
            print(number3, "is second largest")
    else:
        if number1.__gt__(number3):
            print(number1, "is second largest")
        else:
            print(number3, "is second largest")

else:
    print(number3, "is the greatest")
    print(temp, "is second largest")

