import random

# # In this program we will try to make a code on picking up a credit card
# # from a bunch of credit cards.
# # First we are going to take name inputs and separate them.

# Write the names as ONE string, separated by commas
bankers_input = "gopal, niloy, pranto, sojib, nayon"

# Use split(",") to turn that string into a list of names [web:45][web:58]
bankers_name = bankers_input.split(",")

# Remove extra spaces around each name (optional but nice) [web:49]
bankers_name = [name.strip() for name in bankers_name]

# # Get total number of items in list [web:27]
# num_items = len(bankers_name)

# # Pick a random index between 0 and num_items - 1 [web:22][web:32]
# random_choice = random.randint(0, num_items - 1)

# # Get the selected banker’s name
# person_who_will_pay = bankers_name[random_choice]

# print(person_who_will_pay + " is going to buy the meal today.")

will_pay = random.choice(bankers_name)
print(will_pay + " - will pay the bill")
