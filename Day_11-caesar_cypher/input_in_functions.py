def greet():
    print("Hi my name is Gopal Das")
    print('Roll Number is : 22_mkt_030')
    print("Today is 3rd january, 2026")
greet()

def greet_value(name):
    print(f"Hi my name is {name}")
    print(f'Roll Number is : 22_mkt_030')
greet_value("gopal")

#Now Functions With more than 1 input
def values(name, age):
    print(f"your name is : {name}")
    print(f"your Age is : {age}")
values(age= 23, name= "Gopal Das" )