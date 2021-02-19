# class student:
#
#     def add(kit):
#         print("hi")
# s=student()
# s.add()
class Student:
    def __init__(self):
        self.name = ''
        self.m1 = 0
        self.m2 = 0
        self.m3 = 0

    def getdata(self):
        self.name=input("Enter name")
        self.m1 = int(input("Enter mark 1"))
        self.m2 = int(input("Enter mark 2"))
        self.m3 = int(input("Enter mark 3"))

    def printdata(self):
        total=self.m1+self.m2+self.m3
        print(self.name)
        print(total)

s1=Student()
s1.getdata()
Student.printdata(s1)


