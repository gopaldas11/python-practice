#We are going to make a rollercoaster ride if else condition.
print("Welcome to the Rollercoaster Ride: ")
height = int(input("Enter your height in cm = "))
#Now lets apply the conditions.
if height >= 120:
    print("You can ride the Rollercoaster")
    age = int(input("Enter your age: "))
    if age < 12:
        print("You have to pay $5.")
    elif age <= 18:
        print("You have to pay $6.")
    else:
        print("You have to pay $12.")
else:
    print("You can not ride the rollercoaster, sorry")
