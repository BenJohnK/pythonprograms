function add(num1,num2){
    return num1+num2
}
// var sum=add(10,20)
// console.log(sum)

function printPrime(low,upper){
    
    for(let i=low;i<=upper;i++){
        prime=1
        for(let j=2;j<=i/2;j++){
            if(i%j==0){
                prime=0
                
            }
        }
        if(prime==1){
            console.log(i)
        }
        prime=1
    }
}
// printPrime(5,35)

function magicSum(num){
    sum=0
    magicNumber=num
    for(let i=0;i<num;i++){
        sum=sum+magicNumber
        magicNumber=magicNumber*10+num
    }
    console.log(sum)
}
magicSum(3)