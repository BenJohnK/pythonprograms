f=open("demo","r")
# for lines in f:
#     print(lines)

lst=[]
set1=set({})
for lines in f:
    lst.append(lines.rstrip("\n").split(" "))

for ele in lst:
    for i in ele:
        set1.add(i)
print(set1)





