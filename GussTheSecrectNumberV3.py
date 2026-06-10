"""
What this program should do:
    generate a random secret number between 1 and 100
    ask the user to guess the secret number
    if the user guesses wrong, tell them if they are too high or too low
    and keep asking until they guess the secret number
    when they guess the secret number, congratulate them and tell them how many guesses it took
    and give them a message based on how many guesses it took them to guess the secret number
"""
import random

secret_number =   random.randint(1, 100)
number_of_guesses = 0
print("Welcome to the Guess the Secret Number Game!")

while True:
    user_guess = int(input("Please enter your guess (between 1 and 100): "))
    number_of_guesses += 1
    
    if user_guess == secret_number:
        if number_of_guesses == 1:
            print(f"Impressive! You guessed the secret number {secret_number} on your first try! Congratulations!")
        elif number_of_guesses <= 5:
            print(f"Congratulations! You guessed the secret number {secret_number} in {number_of_guesses} guesses! Great job!")
        elif number_of_guesses <= 10:
            print(f"Congratulations! You guessed the secret number {secret_number} in {number_of_guesses} guesses! Not bad! but you can do better!")
        else:
            print(f"Congratulations! You guessed the secret number {secret_number} in {number_of_guesses} guesses! Uhm... you can do better! Don't give up, keep trying!")
        break
    elif user_guess < secret_number:    
        print("guess higher")
    else:
        print("guess lower")
    

print("Thank you for playing the Guess the Secret Number Game!")
    

