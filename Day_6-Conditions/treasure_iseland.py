print('''       .__.      .==========.
     .(\\//).  .-[ for you! ]
    .(\\()//)./  '=========='
.----(\)\/(/)----.
|     ///\\\     |
|    ///||\\\    |
|   //`||||`\\   |
|      ||||      |
|      ||||      |
|      ||||      |
|      ||||      |
|      ||||      |
|      ||||      |
'------====------''')
print("welcome to the treasure island")
print("Your mission is to find the treasure.")
choise1 = input('You \'re at a crossroad. Which way you want to go ? "left" or "right". ').lower()
if choise1 == "left" or "Left":
    choise2 = input('You\'ve come to a lake, There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choise2 == "wait":
        choise3 = input("you arived to the island unharmed, you three doors to choose, one red , one yellow , one blue. which door do you chose? ").lower()
        if choise3 == "red":
            print("Its a room full of fire, game over")
        elif choise3 == "yellow":
            print("Conress tou found the tresure.")
        elif choise3 == "blue":
            print("You chose the door full of beasts.")
        else:
            print("You chose a door that doesn't exist.")
    else:
        print("you got attacked by a elegator")
else:
    print("You fell into a hole, game over...........")