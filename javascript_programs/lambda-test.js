sum=(num1,num2)=>num1+num2
console.log(sum(10,20));
raise4=(num1)=>num1%2==0?num1*2:num1*3
console.log(raise4(3));
var lst=[2,3,7,4,5,6,99]
new_lst=lst.reduce((num1,num2)=>num1>num2?num1:num2)
console.log(new_lst);
console.log(lst)
lst.sort((i,j)=>i-j)
console.log(lst)


