"""
This program should do:
    Ask for the user's name.
    Ask for the user's age and convert the age to an integer.
    Check if the user is an adult (18 or older.
    Then display a greeting with the user's name and whether they are an adult or not.
"""
user_name = input("What is your name? ")
user_age = int(input("What is your age? "))

if user_age >= 18:
    print(f"Hello, {user_name}. You are an adult.")

else: 
    print(f"Hello, {user_name}. You are not an adult.")

print("Goodbye!")
