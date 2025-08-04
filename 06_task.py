# Create a Customer class with name and an empty list purchases. 
# Add a method add_purchase(item) to add items to the list. 
# Also add a show_purchases() method.

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchases = []

    def add_purchase(self, item):
        self.purchases.append(item)

    def show_purchases(self):
        print(f"{self.name} bought: {', '.join(self.purchases)}")

c1 = Customer("Aarav")
c1.add_purchase("Shoes")
c1.add_purchase("Bag")
c1.show_purchases()
