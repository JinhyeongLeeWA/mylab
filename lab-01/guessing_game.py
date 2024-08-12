import random

print("Welcome to the Guessing Game!")

random_number = random.randint(1, 25)
guess = None
while guess != random_number:
    guess = int(input("Guess a number between 1 and 25: "))

    if guess < random_number:
        print("The number is higher than your guess.")
    elif guess > random_number:
        print("The number is lower than your guess.")

print("Congratulations! You guessed the correct number.")
