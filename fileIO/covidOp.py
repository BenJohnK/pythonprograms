f=open("covid.csv","r")
dit={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    state=words[3]
    confirmed_cases=words[-1]
    if state== "Telengana" or state=="Telangana" or state=="Telangana***" or state=="Telengana***":
        state="Telangana"
    dit[state]=int(confirmed_cases)
for k in dit:
    print(k,dit[k])

sorted_data=sorted(dit,key=dit.get,reverse=True)
print(sorted_data)
print(sorted_data[0])
