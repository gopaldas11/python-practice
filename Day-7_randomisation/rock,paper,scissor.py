# We are goin to make a game - ROCK , PAPER , SCISSORS.
# Right now we will import random to make the computer choce randoly for the game.
import random
# Now lets import the ascii code from any website
ascii_art= [""" Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
# Now take user input and if user gives other inputs rather than 0,1,2 printing invaid error
try:
    user_input = int(input("Enter your choice (0 = Rock, 1 = Paper, 2 = Scissors) = "))
except ValueError:
    print("Invalid Input : You have to chose (0 = Rock, 1 = Paper, 2 = Scissors), \nYou have chosen a different value")
    exit()
# Making conditions if the inputs are not in the expercted value to show invalid input.
if user_input not in [0, 1, 2]:
    print("Invalid input: Enter only (0, 1, 2)")
    exit()
# Importing random and commanding the computer to chose anythiing random from the instractions. 
computer_choice = random.randint(0, 2)
# Printing and addressing ascii art
print("\nYou chose: ")
print(ascii_art[user_input])
print("\nComputer choice : ")
print(ascii_art[computer_choice])
# making statements for the program. 
if computer_choice == user_input:
    print("Match Result: DRAW")
elif (
    (user_input == 0 and computer_choice == 2) or
    (user_input == 1 and computer_choice == 0) or
    (user_input == 2 and computer_choice == 1) ):
    print("Congratulations : You Win ")
else:
    print("Ohh! Sorry you lose , Try again next time ")
