import re

f=open("vehiclenos.txt","r")
lst=[]
rule = '[K][L][0-9]{2}[a-zA-Z]{2}[0-9]{4}'
valid_lst=[]
for lines in f:
    word=lines.rstrip("\n")
    lst.append(word)


for x in lst:
    matcher=re.fullmatch(rule,x)
    if matcher is None:
        pass
    else:
        valid_lst.append(x)

print(valid_lst)

fw=open("vehicle_nos_valid.txt","a")

for x in valid_lst:
    fw.write(x+"\n")

f.close()
fw.close()


