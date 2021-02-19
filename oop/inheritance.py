class Parent:
    def m1(self):
        print("m1")

class Child:
    def m1(self):
        print("m2")

class SubChild(Child,Parent):
    def m3(self):
        print("m3")
    def m1(self):
        print("m1 inside SubChild")

sub=SubChild()
sub.m1()

