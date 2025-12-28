# We are going to make a coin toss code.
# import random
# random_integer = random.randint (1, 20)
# print(random_integer)
# num = random.randint (100, 1000)
# print(num)
# random_float = random.random() * 5
# print(random_float) 
import random 
pick = input("What do you chose? Head or Tail?: ").lower()
result = random.randint (0, 1)
if result == 0:
    print("Coin showed - Head.")
else:
    print("Coin Showed - Tail.")