class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Bhau Bhau!")

# Creating objects
dog1 = Dog("Ramu", "Labrador")
dog2 = Dog("Harke", "Pug")
dog3 = Dog("Shyam", "German Shepherd")

# Calling method
dog1.bark()
dog2.bark()
dog3.bark()