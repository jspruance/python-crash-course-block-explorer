# limit max guesses

import random

secret_number = random.randint(1, 100)
max_attempts = 6

for attempts in range(max_attempts):
    guess = int(input("Welcome to the guessing game. Please enter your guess: "))
    print(f"You guessed {guess}")

    if guess > secret_number:
        print("Your guess is too high")

    if guess < secret_number:
        print("Your guess is too low")

    if guess == secret_number:
        break

if guess == secret_number:
    print(f"You guessed the secret number, {secret_number} in {attempts} guesses. You win!")

if guess != secret_number:
    print(f"You're out of guesses. The secret number is {secret_number}")

print("Thanks for playing.")

