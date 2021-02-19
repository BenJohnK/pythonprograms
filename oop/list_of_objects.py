class Student:
    def __init__(self,name,age,course,total):
        self.name=name
        self.age=age
        self.course=course
        self.total=total
    def __str__(self):
        return self.name

students=[]
st=Student("Ajay",23,"mca",100)
st1=Student("Arya",25,"mca",160)
st2=Student("Ben",25,"bca",150)
students.append(st)
students.append(st1)
students.append(st2)
for student in students:
    if student.course=="mca":
        print(student.name)
large=0
name=''
for student in students:
        if student.total>large:
            large=student.total
            name=student.name

print(large, name)