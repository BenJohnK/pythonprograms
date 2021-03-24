class Parent{
    phone(){
        console.log("inside parent")
    }
}
class Child extends Parent{
    phone(){
        console.log("inside child")
    }
}
var ch=new Child()
ch.phone()