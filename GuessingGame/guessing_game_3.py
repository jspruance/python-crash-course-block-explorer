# make the guessing logic loop until game is over

import random

secret_number = random.randint(1, 100)
won_game = False

while won_game != True:
    guess = int(input("Welcome to the guessing game. Please enter your guess: "))
    print(f"You guessed {guess}")

    if guess > secret_number:
        print("Your guess is too high")

    if guess < secret_number:
        print("Your guess is too low")

    if guess == secret_number:
        won_game = True
        print(f"You guessed the secret number, {secret_number}. You win!")

print("Thanks for playing.")