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
var obj2=new Employee(101,"Joel","Engineer",40000)
var obj3=new Employee(102,"Lery","Sales",30000)
var obj4=new Employee(103,"Josh","Engineer",35000)
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
employees.sort((emp1,emp2)=>emp1.salary-emp2.salary)
console.log(employees)
var max_sal=employees.reduce((n1,n2)=>n1.salary>n2.salary?n1.salary:n2.salary)
console.log(max_sal)

