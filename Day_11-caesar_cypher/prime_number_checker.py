# prime checker

def prime_chcker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Its a prime Number.")
    else:
        print("Its Not a prime number.")
while True:
    n = int(input("Enter a number (or -1 to quit): "))
# To exit condition
    if n == -1:          
        print("Goodbye!")
        break
    prime_chcker(number = n)
 