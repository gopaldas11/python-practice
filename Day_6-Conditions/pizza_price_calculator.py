# In this programe we are going to code about a pizza price calculator.
# first lets take inputs.
size = input("What size pizza you want? S, M or L: ")
want_pepperoni = input("Do you want pepperoni? yes or no: ")
extra_cheese = input("Do you want extra cheese? yes of no: ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if want_pepperoni == "yes":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "yes":
    bill += 1
print(f"Your final bill is ${bill}")