num1=10
num2=20
num3=5
temp=0
flag=0
if(num1>num2){
    temp=num1
}
else{
    temp=num2
}
if(num3>temp){
    console.log("largest no: "+num3)
    console.log("second largest: "+temp)
}
else{
    console.log("largest no: "+temp)
    if(temp==num1){
        if(num3>num2){
            console.log("second largest: "+num3)
        }
        else{
            console.log("second largest: "+num2)
        }
    }
    else{
        if(num3>num1){
            console.log("second largest: "+num3)
        }
        else{
            console.log("second largest: "+num1)
        }
    }
}
