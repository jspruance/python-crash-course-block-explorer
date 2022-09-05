# generate secret random number
# compare secret number to guess

import random

secret_number = random.randint(1, 100)

guess = int(input("Welcome to the guessing game. Please enter your guess: "))
print(f"You guessed {guess}")

if guess > secret_number:
    print("Your guess is too high")
elif guess < secret_number:
    print("Your guess is too low")
else:
    print(f"You guessed the secret number: {secret_number}. You win!")