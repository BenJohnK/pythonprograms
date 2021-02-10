text="hello hello hi hi hi how hi hello"
words=text.split(" ")
dict={}
print(words)
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
large=0
name=""
for ele in dict:
    if dict[ele]>large:
        large=dict[ele]
        name=ele
print(name)

