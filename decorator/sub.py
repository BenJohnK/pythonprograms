def wrapper(sub):
    def inner(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
        return sub(num1,num2)
    return inner

@wrapper
def sub(num1,num2):
    return num1-num2
print(sub(10,20))