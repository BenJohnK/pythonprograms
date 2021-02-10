text="abbac"
dict={}
for x in text:
    if x in dict:
        dict[x]+=1
        print(x)
        break
    else:
        dict[x]=1

