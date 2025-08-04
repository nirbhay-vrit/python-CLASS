# Create a Teacher class with a name. 
# Then create a Subject class that takes a subject name and a Teacher object. 
# Add a method to print something like:
# “Math is taught by Ms. Rita.”

class Teacher:
    def __init__(self, name):
        self.name = name

class Subject:
    def __init__(self, name, teacher: Teacher):
        self.name = name
        self.teacher = teacher

    def info(self):
        print(f"{self.name} is taught by Ms. {self.teacher.name}.")

t1 = Teacher("Rita")
s1 = Subject("Math", t1)
s1.info()
