
number = int(input("Enter number: "))
def check_prime_number(n):
    is_prime = True
    for i in range(2,n):
        print(i)
        if n % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



check_prime_number(number)
