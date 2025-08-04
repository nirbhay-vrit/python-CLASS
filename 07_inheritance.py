class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} engine started.")

class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand} is charging...")

ecar = ElectricCar("Tesla")
ecar.start()
ecar.charge()
