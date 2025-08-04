class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_no}) - Avg: {self.average():.2f}"

s1 = Student("Alice", 101)
s1.add_grade(80)
s1.add_grade(90)

s2 = Student("Bob", 102)
s2.add_grade(70)
s2.add_grade(75)
s2.add_grade(85)

print(s1)
print(s2)