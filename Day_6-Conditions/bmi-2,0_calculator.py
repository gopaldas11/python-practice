# Now we are going to practice BMI 2. 0 calculator.
print("Hello, Welcome to the BMI calculator\nHope your days are going well.")
#First lets take inputs.
height = float(input("Enter your height in m= "))
weight = int(input("Enter your weight in kg= "))
#now lets make the calculations.
true_bmi = round(weight / (height ** 2), 2)
if true_bmi < 18:
    print(f"Your BMI is {true_bmi}, You are Undereright.")
elif true_bmi  < 25:
    print(f"Your BMI is {true_bmi}, You are Healthy & Normal. ")
elif true_bmi < 30:
    print(f"Your BMI is {true_bmi}, You are overweight.")
elif true_bmi < 35:
    print(f"Your BMI is {true_bmi}, You are Obese.")
else: 
    print(f"Your BMI is {true_bmi}, You are Clinically Obese.")