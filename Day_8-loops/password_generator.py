# we will be writing a program that can generate strong passwords
import random
latters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the pass word generator. ")
lett = int(input(" How many Latters do you want in your Password? : \n"))
symb = int(input("How many Symbols do you want in your Password? : \n"))
nums = int(input("How many Numbers do you want in your Password? : \n"))

password_list = []
for char in range(1, lett + 1):
    password_list.append(random.choice(latters) )
for char in range(1, symb + 1):
    password_list.append(random.choice(symbols)) 
for char in range(1, nums + 1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = ""
for charecter in password_list:
    password += charecter
print(f"Your password is : ", password)