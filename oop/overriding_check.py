class Student:
    def show(self,a,b):
        print("no arguments")
class Sub(Student):
    def show(self):
        print("in sub")

s=Sub()
s.show(10,20)