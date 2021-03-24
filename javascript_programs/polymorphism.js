class Math{
    add(){
        console.log("inside first")
    }
    add(no1,no2){
        console.log("inside second")
    }
    add(no1,no2,no3){
        console.log("inside third")
    }
}

var obj= new Math()
obj.add(10,20,30,40)