# exception keywords in python are try,except,finally

num1=int(input("Enter number 1"))
num2=int(input("Enter number 2"))

try:
    res=num1/num2
except Exception as e:
    print(e.args)

print("After everything")