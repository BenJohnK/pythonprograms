number1=int(input("Enter number 1"))
number2=int(input("Enter number 2"))
number3=int(input("Enter number 3"))
if number1.__gt__(number2):
    temp = number1
    f = 0
else:
    temp = number2
    f = 1
if temp.__gt__(number3):
    print(temp)
    if f == 0:
        if number2.__gt__(number3):
            print(number2)
            print(number3)
        else:
            print(number3)
            print(number2)
    else:
        if number1.__gt__(number3):
            print(number1)
            print(number3)
        else:
            print(number3)
            print(number1)

else:
    print(number3)
    if temp == number1:
        print(number1)
        print(number2)
    else:
        print(number2)
        print(number1)


