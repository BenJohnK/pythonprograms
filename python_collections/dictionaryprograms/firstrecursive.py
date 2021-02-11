text="abac"
dict={}
for x in text:
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1
f=0
print(dict)

for x in dict:
    if dict[x]==1:
        f=1
        print(x)
if f==0:
    print("No non-recursive character")

data=sorted(dict,key=dict.get)     #sorting dictionary
print(data)





