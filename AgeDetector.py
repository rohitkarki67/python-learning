'''
What this program should do:
    Ask for the user's name.
    Ask for the user's age.
    Convert the age to an integer.
    Calculate next year's age.
    Display a greeting.
    Display next year's age.

'''

user_name = input("What is your name? ")
user_age = int(input("What is your age? "))

user_next_year_age = user_age + 1

print(f"Hello, {user_name}.")
print(f"Next year you will be {user_next_year_age} years old!")