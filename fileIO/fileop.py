f=open("demo","r")
# for lines in f:
#     print(lines)

lst=[]
set1=set({})
for lines in f:
    lst.append(lines.strip("\n").split(" "))
lst2=[]
for ele in lst:
    for i in ele:
        lst2.append(i)
print(lst2)

dit={}
for word in lst2:
    if word in dit:
        dit[word]+=1
    else:
        dit[word]=1
print(dit)

data=sorted(dit,key=dit.get,reverse=True)
print(data[0])

lst3=["This","the","where","when","is","have","with","they","may","but","no","of","and"]

# n=int(input("Enter how many words to remove"))
# for i in range(n):
#     x=input("Enter word")
#     lst3.append(x)
# for word in lst3:
#     if word in dit:
#         dit.pop(word)
# print(dit)
for word in lst3:
    if word in dit:
        dit.pop(word)
print(dit)





