# Create a class Chair with a class variable legs = 4, and instance variables material and 
# color. Add a method describe() to print a sentence like:
# “This is a red wooden chair with 4 legs.”


class Chair:
    legs = 4

    def __init__(self, material, color):
        self.material = material
        self.color = color

    def describe(self):
        print(f"This is a {self.color} {self.material} chair with {Chair.legs} legs.")

chair1 = Chair("wooden", "red")
chair1.describe()
