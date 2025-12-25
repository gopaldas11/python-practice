# Calculator of - Your life in weeks.
# We are making a calculator that gives number outputs of days , weeks , months are left in a persons life when he enters his age.
age = int(input("Enter your age in years: "))
remaining = (90 - age) 
days = remaining * 365
weeks = remaining * 52
months = remaining * 12
data = (f"You have days to live {days}, You have months to live {months}, You have weeks to live {weeks}")
print(data)