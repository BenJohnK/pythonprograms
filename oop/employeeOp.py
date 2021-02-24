class employee:
    def __init__(self,id,name,designation,exp,salary):
        self.id=id
        self.name=name
        self.designation=designation
        self.experience=exp
        self.salary=salary
    def __str__(self):
        return self.name
from functools import reduce
employeelist=[]
f=open("employees","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    id,name,designation,exp,salary=data
    emp=employee(id,name,designation,exp,salary)
    employeelist.append(emp)

# for x in employeelist:
#     print(x)

#who are developers?

developers=list(filter(lambda emp:emp.designation=="developer",employeelist))
for person in developers:
    print(person)

# who has the highest salary?

maxsal=max(list(map(lambda emp:emp.salary,employeelist)))
maxsalperson=list(filter(lambda emp:emp.salary==maxsal,employeelist))
# print(maxsalperson)
for x in maxsalperson:
    print(x,maxsal)

# persons whose name starts with a

names_a=list(filter(lambda emp:emp.name[0]=="a",employeelist))
for x in names_a:
    print(x)

#sum of salaries of all developers

# sum=reduce(lambda emp1,emp2:emp1.salary+emp2.salary,employeelist)
# print(sum)

sal_list=list(map(lambda emp:emp.salary,employeelist))
print(sal_list)

def sub_smart(fun):
    def inner(no1,no2):
        if no2>no1:
            (no1,no2)=(no2,no1)
        return fun(no1,no2)
    return inner

@sub_smart
def sub(no1,no2):
    return no1-no2

print(sub(10,20))
