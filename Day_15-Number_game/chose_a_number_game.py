# Computer secretly chooses one random number within a defined range (e.g., 1–100).
# Player cannot see the number.
# Player selects a difficulty mode:
    # Easy → 10 wrong guesses allowed
    # Hard → 5 wrong guesses allowed
# Player keeps guessing until:
    # They guess correctly → WIN
    # They run out of attempts → LOSE
import random
from art import logo
print(logo)
print("Welcome to the Number Catching game.\n")
print("You have to guess a number that computer has randomly selected from 0 to 100.\n")
print("You have 2 Mode: Easy and Hard. ")
secret_number = random.randint(1, 100)
mode_points = {
    "easy": 10,
    "hard": 5
}
choice = input("What mode do you chose? 'EASY' or 'HARD' : ").lower()
if choice not in mode_points:
    print("Invalid Choice")
    exit()
chances = mode_points[choice]
while chances > 0:
    guess = int(input("Guess the number from 1 to 100: "))
    if guess == secret_number:
        print(f"Congratulations😎 ! You Win {secret_number}: is the number.")
        break
    elif guess > secret_number:
        print("Too High...")
    else:
        print("Too Low...")
    chances -= 1
    print(f"chances left : {chances}")
if chances == 0:
    print(f"You lost!...The Number Was: {secret_number}.")
    print(logo)