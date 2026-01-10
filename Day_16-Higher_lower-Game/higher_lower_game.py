import random
from art import logo, vs
from game_data import data
print("This is a 'Higher'-'Lower' Game. ")
print(logo)
score = 0
game_over = False
while not game_over:
    random.shuffle(data)
    choice_1 = random.choice(data)
    choice_2 = random.choice(data)
    while choice_1 == choice_2:
        choice_2 = random.choice(data)
    print(f"1: {choice_1['name']}, a {choice_1['description']}.")
    print(vs)
    print(f"2: {choice_2['name']}, a {choice_2['description']}.\n")
    selected = int(input("Who has the Highest Follower?\n  Type '1' = for choice - 1. \nor\n '2' = for choice - 2.  your Choice? : "))

    compear_1 = choice_1['follower_count']
    compear_2 = choice_2['follower_count']
    if compear_1 > compear_2:
        correct_ans = 1
        correct_choice = [choice_1]
        correct_followers = [compear_1]
    else:
        correct_ans = 2
        correct_choice = [choice_2]
        correct_followers = [compear_2]
    if selected == correct_ans:
        score += 1
        print(f"correct!. The highest followr has {correct_choice} with - {correct_followers} follower, Your Score: {score}")
    else:
        print(f"Wrong!. The highest followr has: {correct_choice} with - {correct_followers} follower, Your Score: {score}")
        game_over = True

        
     