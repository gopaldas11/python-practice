# we are going to make a BMI calculator. 
hight = input("Enter your hight in m: ")
weight = input("Enter your weight in kg: ")
# We have to use type of every kind of data, ex: weight = int  & height = float
bmi = int(weight) // float(hight) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
