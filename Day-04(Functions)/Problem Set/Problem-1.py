# 1. Check if a number is prime
def is_prime(n):
    if n == 0:
        return "Number is zero"
    elif n <= 2:
        return "Number is prime"
    else:
        for i in range(3, (n**0.5) + 1):
            if n % i == 0:
                return "It is not a prime number"
            else:
                return "It is a prime number"
