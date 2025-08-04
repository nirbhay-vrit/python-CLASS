class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.brand} {self.model} engine started.")

    def show_details(self):
        print(f"{self.year} {self.brand} {self.model}")

# Create instances
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model 3", 2023)

car1.start_engine()
car2.show_details()
