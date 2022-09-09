def prime_check(number):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                return "This is not a prime number."
        else:
            return "This is a prime number"
    else:
        return "This is not a prime number."

print(prime_check(int(input('Enter a number to test:'))))