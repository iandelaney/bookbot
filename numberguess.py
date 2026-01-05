import random

chosen_number = random.randint(1, 100)
lives = 10
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 10 attempts to guess it")

while lives > 0:
    guess = input("Guess a round number between 1 and 100 ")
    if guess == "":
        print("That wasn't a number.")
        continue
    try:
        guess = int(guess)
    except ValueError:
        print("That wasn't a number.")
        continue
    if guess == chosen_number:
        print(f"🎉 Congratulations! You guessed the number in {11 - lives} attempts!")
        break
    elif guess > chosen_number:
        print("Go lower ⬇️")
    elif guess < chosen_number:
        print("Go higher ⬆️")
    lives -= 1

print(f"You are dead now :( The number you wanted was {chosen_number}")