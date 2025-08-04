class Bike:
    wheels = 2  # Class variable (shared)

    def __init__(self, brand, color):
        self.brand = brand      # Instance variable
        self.color = color

    def ride(self):
        print(f"Riding a {self.color} {self.brand} with {Bike.wheels} wheels.")

bike1 = Bike("Yamaha", "Blue")
bike2 = Bike("Honda", "Red")

bike1.ride()
bike2.ride()
