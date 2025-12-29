import random
art = [""" Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
""" Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
try:
    user_num = int(input("Enter a number : ( 0 = rock, 1 = paper, 2 = scissors)\n:"))
except ValueError:
    print("Invalid Input")
    exit()
if user_num not in [0, 1, 2]:
    print("Invalid error. please enter 0 or 1 or 2 to play.")
    exit()
computer_choice = random.randint(0, 2)
print("\n Your choice")
print(art[user_num])
print("\n Computer choice")
print(art[computer_choice])
if computer_choice == user_num:
    print("Match result = DRAW")
elif (
    (user_num == 0 and computer_choice == 2) or
    (user_num == 1 and computer_choice == 0) or
    (user_num == 2 and computer_choice == 1)):
    print("Congratulations: YOU WIN")
else:
    print("Sorry, YOU LOSE")
