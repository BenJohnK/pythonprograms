class Student{

    setPerson(id,name,age){
        this.id=id
        this.name=name
        this.age=age
    }
    printPerson(){
        console.log(this.id+this.name+this.age)
    }
}
var s1=new Student()
s1.setPerson(100,"ben",25)
s1.printPerson()