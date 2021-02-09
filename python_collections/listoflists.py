employee=[
    [100,"Anil","developer",5000,1989,1995],
    [101,"Sundar","Dev",50000,1970,1990],
    [102,"Anand","ev",6000,1989,1991],
    [105,"Akash","developer",60000,1990,1999],
]

maxsal=max(list(map(lambda em:em[3],employee)))
print(maxsal)

#print only names
for emp in employee:
    print(emp[1])
print()
for emp in employee:
    print(emp[3])
print()
for emp in employee:
    if(emp[2]=="developer"):
        print(emp)

sum=0
total=0
for emp in employee:
    sum=sum+emp[3]
print(sum)

large=0
for emp in employee:
    if emp[3]>large:
        large=emp[3]
print(large)
lst2=[]
for emp in employee:
    lst2.append(emp[3])
print(max(lst2))
#print employees worked in 1990s
#print experience of each developer
#print employee with highest salary
lst2=[]
print("Experience of each developers")
for emp in employee:
    lst2.append(emp[5]-emp[4])
    print(emp[5]-emp[4])
print("Highest Experience")
print(max(lst2))
c=lst2.index(max(lst2))
print(employee[c])
lst3=[]
for emp in employee:
    if emp[4] >= 1990 and emp[5]<2000:
        lst3.append(emp[1])
print("Employees worked in 1990s")
for x in lst3:
    print(x)

