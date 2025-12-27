# lets practice the codes
year = int(input("What is the year: "))
#After taking the input we will make the conditions.
# Which are - (year % 4 == 0 : Yes leap year) (Year % 100 == 0: is and is no - leap year) (year % 400 == 0: yes leap year) 
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is Not a leap year")