class Vehicle:
    def start(self):
        print("Vehicle starts")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


obj = ElectricCar()
obj.start()
obj.drive()
obj.charge()
