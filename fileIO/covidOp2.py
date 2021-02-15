f=open("covid.csv", "r")
dit={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    state=words[3]
    cases=int(words[-1])
    dit[state]=cases
print(dit)
for k in dit:
    print(k,dit[k])

sorteddit=sorted(dit,key=dit.get,reverse=True)
print(sorteddit)
