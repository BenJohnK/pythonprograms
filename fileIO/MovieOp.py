f = open("movies.csv","r")
dit={}
for lines in f:
    words = lines.rstrip("\n").split(",")
    year=words[2]
    if year in dit:
        dit[year]+=1
    else:
        dit[year]=1

print(dit)
print((max(dit,key=dit.get)))


