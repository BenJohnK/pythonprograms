var numbers=[10,20,30,40]
for(let num of numbers){
    console.log(num)
}
numbers.push(2)
// for(num of numbers){
//     console.log(num)
// }
numbers.sort()  //this wont work for sort the list
for(let num of numbers){
    console.log(num)
}
numbers.sort((i,j)=>i>j?-1:1)
console.log(numbers)
