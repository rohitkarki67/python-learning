"""
What this program should do:
- Set a secret number
- Ask the user to guess the secret number
- If the user guesses the secret number, print a congratulatory message
- If the user does not guess the secret number, print a message they guessed wrong.

"""


secret_number = 7 # Hehehe Ronaldo jersey number

print("Hey there! Can you guess the secret number between 1 to 10?")

user_inpit = float(input("Enter your guess: "))

if user_inpit == secret_number:
    print("Great you gussed right.")

else:
    print("You gussed it wrong.")