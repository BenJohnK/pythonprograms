from functools import reduce
sum=lambda num1,num2:num1+num2
print(sum("hello ","lery"))
square_cube=lambda num1:num1**2 if num1%2==0 else num1**3 
print(square_cube(4))
lst=[2,4,5,7]
new_lst=list(map(lambda num1:num1+1 if num1%2==0 else num1-1,lst))
print(new_lst)
odd_lst=list(filter(lambda num1:num1%2!=0,lst))
print(odd_lst)
even_lst=list(filter(lambda num1:num1%2==0,lst))
print(even_lst)
highest=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(highest)







