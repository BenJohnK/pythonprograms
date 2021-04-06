lst=[2,3,4,5,6]
squares=[x**2 for x in lst]
print(squares)
squares=[x**2 if x%2==0 else x**3 for x in lst]
print(squares)
