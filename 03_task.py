# Create a Laptop class with brand, model, and year. Add a method show_specs() to print all the details.

class Laptop:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_specs(self):
        print(f"{self.year} {self.brand} {self.model}")

laptop1 = Laptop("Dell", "XPS 13", 2021)
laptop1.show_specs()
