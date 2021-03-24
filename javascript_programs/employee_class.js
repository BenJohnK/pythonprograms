class Employee{
    constructor(id,name,depart,salary){
        this.id=id
        this.name=name
        this.depart=depart
        this.salary=salary
    }

}

var employees=[]
var obj1=new Employee(100,"Ben","Engineer",40000)
var obj2=new Employee(101,"Joel","Engineer",20000)
var obj3=new Employee(100,"Lery","Sales",30000)
var obj4=new Employee(100,"Josh","Engineer",35000)
employees.push(obj1)
employees.push(obj2)
employees.push(obj3)
employees.push(obj4)
var employees_name_list=employees.map(obj=>obj.name)
console.log(employees_name_list)
var employees_name_engineer=employees.filter(obj=>obj.depart=="Engineer").map(obj=>obj.name)
console.log(employees_name_engineer)
var employees_name_salary=employees.filter(obj=>obj.salary>30000).map(obj=>obj.name)
console.log(employees_name_salary)


