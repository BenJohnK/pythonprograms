st=set({})
print(type(st))
st={10,20,30,True,"hello"} #indexing is not possible with set
st2={5,15}
st.update(st2)

print(st)