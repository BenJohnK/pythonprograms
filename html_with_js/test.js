clicked=false
function clickedOn(){
    if(clicked==false){
        for(i=0;i<5;i++)
        {   
            document.getElementById("main").innerHTML+='<p>hi</p>'
        }
    }   
    else{
        document.getElementById("main").innerHTML="";
    }
    clicked=!clicked
}
console.log("welcome")
var comp_name = "LeryBen"
console.log("company name is "+comp_name);
var name="Ben"
var age=18
console.log(`My name is ${name} and I am ${age} years old`);


var total=150
var average= 47.75
var name="ajay"
var isActive=true
console.log(typeof(total))
console.log(typeof(average))
console.log(typeof(name))
console.log(typeof(isActive))

if(total>0){
    console.log("+ve")
}
else if(total==0){
    console.log("zero")
}
else{
    console.log("-ve")
}


number=9
// if(number%3==0&&number%15!=0){
//     console.log("fiz")
// }
// if(number%5==0&&number%15!=0){
//     console.log("bus")
// }
// if(number%15==0){
//     console.log("fizbus")
// }

if(number%15==0){
    console.log("fizbuz")
}
else if(number % 5==0){
    console.log("buz")
}
else{
    console.log("fiz")
}



