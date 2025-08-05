def safe_divide_if(a, b):
    if b == 0:
        print("Cannot divide by zero! (Handled by if)")
    else:
        result = a / b
        print(f"Result: {result}")

print("\nUsing if-elif-else:")
# safe_divide_if(10, 2)  # Works fine
safe_divide_if(5, 0)   # Handles zero denominator




def safe_divide_try(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except Exception as e:
        print(f"Something went wrong: {e}")

print("\nUsing try-except:")
# safe_divide_try(10, 2)  # Works fine
safe_divide_try(5, 0)   # Handles zero denominator




# yo tala ko code chai program crash garxa, test garda vayo, tara for now, i'll comment out

# def convert_and_divide_if_no_check(a, b):
#     if b == 0:
#         print("Cannot divide by zero! (if-else check)")
#     else:
#         result = a / b
#         print(f"Result: {result}")

# print("\nNo validation function — will crash on bad input:")
# convert_and_divide_if_no_check("five", "zero")  # Raises ValueError and crashes




def convert_and_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except Exception as e:
        print(f"Something went wrong: {e}")

print("\nExample with exception handling unexpected input:")
convert_and_divide(10, 2)    # Works
convert_and_divide("five", "0")  # Catches invalid number input




def open_and_divide(a, b):
    try:
        print("Calculation Started...")
        result = a / b
        print(f"✅ Result: {result}")
    except Exception as e:
        print(f"Something went wrong: {e}")
    finally:
        print("🔵 Calculation Terminated... This always runs.")

print("\n--- Example 1: No Error ---")
open_and_divide(10, 2)

print("\n--- Example 2: Division by Zero ---")
open_and_divide(5, 0)




def can_he_vote(name, age):
    try:
        if age >= 18:
            print(f"{name} CAN Vote")
        else:
            print(f"{name} CANT Vote")
    except Exception as e:
        print(f"Something went wrong: {e}")
    finally:
        print("Voting Eligibility Calculated!!!")


# can_he_vote("Ram","TEN")
can_he_vote("Hari",20)



def can_he_vote(name, age):
    try:
        if int(age) >= 18:
            print(f"{name} CAN Vote")
        else:
            print(f"{name} CANT Vote")
    except Exception as e:
        print(f"Something went wrong for {name}: {e}")
    finally:
        print("Voting Eligibility Calculated!!!\n")

can_he_vote("Ram","Ten")
can_he_vote("Hari",20)
can_he_vote("Sita",17)


people = [
    ("Ram", "TEN"),
    ("Hari", 20),
    ("Sita", 17),
    ("Gita", 19),
    ("John", "21"),
    ("Bob", "Eighteen")
]
# print(people)
# Loop through the list
for name, age in people:
    can_he_vote(name, age) 




try:
    print(10/0)
except Exception as error:
    print(f"exception: {error}")
finally:
    print("finally")

a="apple"
a=int("10")