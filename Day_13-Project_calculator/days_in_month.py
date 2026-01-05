# lets practice the codes
#After taking the input we will make the conditions.
# Which are - (year % 4 == 0 : Yes leap year) (Year % 100 == 0: is and is no - leap year) (year % 400 == 0: yes leap year) 
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                    return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_in_month(year, month):
    """ This is a example of docstrings """
    month_days = [31, 28 , 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
         

year = int(input("What is the year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)