lst=[2,3,4,5,6]
lst2=[3,4,5,6,8]
square_list=[num**2 for num in lst]

print(square_list)

even=[num for num in lst2 if num%2==0]
print(even)

pair_lst=[[num,num1] for num in lst for num1 in lst2]
print(pair_lst)

common_lst=[num for num in lst for num1 in lst2 if num==num1]
print(common_lst)

lst=[[10,20],[30,40],[50,60]]
new_lst=[k for num in lst for k in num]
print(new_lst)

sum=[num+1 if num>5 else num-1 if num<5 else num for num in lst2]
print(sum)