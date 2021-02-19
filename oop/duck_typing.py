class Person:
    def drive(self,car):
        car.start()
        car.accel()
        car.stop()

class swift:
    def start(self):
        print("swift car started")
    def accel(self):
        print("swift car accelerated")
    def stop(self):
        print("swift car stopped")
class seltos:
    def start(self):
        print("seltos car started")
    def accel(self):
        print("seltos car accelerated")
    def stop(self):
        print("seltos car stopped")

sw=swift()
p=Person()
p.drive(sw)

