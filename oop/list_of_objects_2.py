class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def check_course(self):
        if self.course=="bca":
            print(self.name)

students=[]
n=int(input("Enter no. of student  objects"))
i=0
while i<n:
    name=input("Enter name")
    age=int(input("Enter age"))
    course=input("Enter course")
    students.append(Student(name,age,course))
    i+=1
for student in students:
    student.check_course()