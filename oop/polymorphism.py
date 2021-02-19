# class Maths:
#     def add(self):
#         print("inside no arguments")
#     def add(self,m1):
#         print("inside one argument")
#     def add(self,m1,m2):
#         print("inside two arguments")
#
# m=Maths()
# m.add()

# class Maths:
#     def add(self,m1=None,m2=None):     #we solve this problem by this trick of assinging none
#         print("inside no arguments")
#
#
# m=Maths()
# m.add(10)

#method overriding

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name

s=Student("Ajay",23)
print(s)
print(s.__str__())