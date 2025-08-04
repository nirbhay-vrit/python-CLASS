# Create a class called Cat that takes name and color, and has a method meow() that prints 
# "<name> says: Meow!"

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print(f"{self.name} says: Meow!")

cat1 = Cat("Luna", "Black")
cat1.meow()