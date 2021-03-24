class Parent{
    m1(){
        console.log("m1")
    }
}
class Child extends Parent{
    m2(){
        console.log("m2")
    }
}
class Subchild extends Child{
    m3(){
        console.log("m3")
    }
}
var sub= new Subchild()
sub.m1()