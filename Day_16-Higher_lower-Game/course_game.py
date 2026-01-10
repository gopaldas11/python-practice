import random
from art import logo, vs
from game_data import data
print("This is a 'Higher'-'Lower' Game. ")
print(logo)
score = 0
game_over = True
def formet_data(account): 
    """ Formet the account data into printable formet."""
    account_name = account['name']
    account_discrip = account['description']
    return f"{account_name}, {account_discrip}"
def check_ans(guess, a_followers, b_followers):
    """ Check the users guess and folowers count and returns if the user is right. """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
account_b = random.choice(data)
while game_over:   
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Choice A : {formet_data(account_a)}")
    print(vs)
    print(f"Choice B : {formet_data(account_b)}")
    guess = input("Who has more followers? 'A' or 'B' :").lower()
    a_follower_count = account_a['follower_count']
    b_follower_count = account_a['follower_count']
    is_correct = check_ans(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You'r correct. Current score {score}.")
    else:
        game_over = False
        print(f"Sorry! You'r Wrong. Final Score {score}.")
