#We are going to make a rollercoaster ride if else condition.
print("Welcome to the Rollercoaster Ride: ")
height = int(input("Enter your height in cm = "))
#Now lets apply the conditions.
if height >= 120:
    print("You can ride the Rollercoaster")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Childs tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Young tickets are $7.")
    elif age >= 46 and age <= 55:
        bill = 0
        print("Everythings gonna be ok, have a free ride on us. ")
    else:
        bill = 12
        print("Adult tickets are $12.")
    want_photo  = input("Do you want a photo taken? Type - Y or N : ")
    if want_photo == "Y":
        bill += 3
        print(f"Your final bill is ${bill}")
else:
    print("You can not ride the rollercoaster, sorry")