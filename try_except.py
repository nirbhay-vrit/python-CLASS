def safe_divide_if(a, b):
    if b == 0:
        print("Cannot divide by zero! (Handled by if)")
    else:
        result = a / b
        print(f"Result: {result}")

print("\nUsing if-elif-else:")
safe_divide_if(10, 2)  # Works fine
safe_divide_if(5, 0)   # Handles zero denominator

# def safe_divide_try(a, b):
#     try:
#         result = a / b
#         print(f"Result: {result}")
#     except ZeroDivisionError:
#         print("Cannot divide by zero! (Handled by exception)")

# print("\nUsing try-except:")
# safe_divide_try(10, 2)  # Works fine
# safe_divide_try(5, 0)   # Handles zero denominator



# def convert_and_divide_if_no_check(a, b):
#     a = float(a)  # Could raise ValueError here!
#     b = float(b)
#     if b == 0:
#         print("Cannot divide by zero! (if-else check)")
#     else:
#         result = a / b
#         print(f"Result: {result}")

# print("\nNo validation function — will crash on bad input:")
# convert_and_divide_if_no_check("five", "0")  # Raises ValueError and crashes




# def convert_and_divide(a, b):
#     try:
#         a = float(a)  # might raise ValueError
#         b = float(b)
#         result = a / b
#         print(f"Result: {result}")
#     except ZeroDivisionError:
#         print("Cannot divide by zero!")
#     except ValueError:
#         print("Please enter valid numbers!")

# print("\nExample with exception handling unexpected input:")
# convert_and_divide("10", "2")    # Works
# convert_and_divide("five", "0")  # Catches invalid number input



# def open_and_divide(a, b):
#     try:
#         print("Opening resource (simulated)...")
#         result = a / b
#         print(f"✅ Result: {result}")
#     except ZeroDivisionError:
#         print("❌ You can't divide by zero!")
#     finally:
#         print("🔵 Closing resource (simulated)... This always runs.")

# print("\n--- Example 1: No Error ---")
# open_and_divide(10, 2)

# print("\n--- Example 2: Division by Zero ---")
# open_and_divide(5, 0)





# def convert_and_divide(a, b):
#     try:
#         a = float(a)  # might raise ValueError
#         b = float(b)
#         result = a / b
#         print(f"Result: {result}")
#     except Exception as e:
#         print(f"Something went wrong: {e}")

# convert_and_divide("10", "2")    # Works
# convert_and_divide("five", "0")