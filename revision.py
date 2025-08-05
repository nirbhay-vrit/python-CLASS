def can_he_vote(age, name="Person With NO name"):
    if age>=18:
        print(f"{name} CAN vote as s/he is {age} years old")
    else:
        print(f"{name} CANT vote as s/he is only {age} years old")

ages = [15,18,30,80,9]

names_ages=[
    ("ram",15),
    ("shyam",18),
    ("hari",30),
    ("geeta",80),
    ("mohan",9)
]
for age in ages:
     can_he_vote(age)

for name, age in names_ages:
        can_he_vote(age,name)