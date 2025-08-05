class Dog:
    def __init__(self, name1234, breed):
        self.name = name1234
        self.breed = breed

    # def __str__(self):
    #     return f"name is: {self.name} and breed is: {self.breed}"

    def bark(self):
        print(f"{self.name} says: Bhau Bhau!")

# Creating objects
dog1 = Dog("Ramu", "Labrador")
# print(dog1.breed)
dog2 = Dog("Harke", "Pug")
dog3 = Dog("Shyam", "German Shepherd")

# Calling method
dog1.bark()
dog2.bark()
dog3.bark()