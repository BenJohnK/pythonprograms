from functools import reduce

lst=[2,3,4,5,6]

sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)

max=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(max)