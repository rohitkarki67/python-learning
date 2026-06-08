'''
what this program does:
secret_number = 7
Ask for a guess
Convert to a number
Use:
if
elif
else
and give feedback to the user
'''

secret_number = 7 # Hehehe Ronaldo jersey number

user_guess = int(input("Guess the secret natural number between 1 and 10: "))

if user_guess == secret_number:
    print("Congratulations! You guessed the secret number!")

elif user_guess < secret_number:
    print("Please try again. Your guess is lower than the secret number.")
else:
    print("Please try again. Your guess is higher than the secret number.")