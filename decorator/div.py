def div(fun):
    def inner(num1, num2):
        if num1 < num2:
            num1, num2 = num2, num1
            return fun(num1,num2)
    return inner


@div
def division(num1, num2):
    return num1 / num2

print(division(10,30))

