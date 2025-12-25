# we are going to make a tip calculator, that will
#combine data like - total bill , percentage of tip, and total parson sharing it.
#First we are taking inputs.
print("Wlcome to the tip calculator")
bill = float(input("Enter the total bill you have to pay: "))
tip = int(input("What percentage tip would you like to give ? 10, 18 or 24? "))
people = int(input("How many people to split the bill: "))
#now we will do our calculations.
calcul_1 = (bill + bill * (tip / 100))
calcul_final = calcul_1 / people
Final_number = "{:.2f}".format(calcul_final, 2)
print(f"Each person should pay $: {Final_number}")
