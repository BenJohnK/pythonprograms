def add(num1,num2):
    return num1+num2

# def add(*num):
#     print(num)
#     sum=0
#     for x in num:
#         sum=sum+x
#     print(sum)
# add(10,20,30,40)

def sum(**kwargs):
    print(kwargs)
    print(kwargs["first"]+kwargs["second"])

sum(first=10,second=30)




