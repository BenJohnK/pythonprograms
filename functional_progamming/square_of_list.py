lst=[1,2,3,4,5]

squares=list(map(lambda num1:num1**2,lst))
print(squares)

print(lst)
lst2=["ben","joel"]

upper=list(map(lambda x: x.upper(),lst2))
print(upper)

numbers=[4,8,9,3,2]

new_numbers=list(map(lambda x: x+1 if x>5 else x-1,numbers))
print(new_numbers)

marks=[35,50,60,20]
result=list(map(lambda x: True if x>=50 else False,marks))
print(result)

lst3=[2,3,4,6]
new_lst=list(filter(lambda x:x%2==0,lst3))
print(new_lst)

names=["ben","joel","apple"]
new_names=list(filter(lambda x: x[0]=='a',names))
print(new_names)

