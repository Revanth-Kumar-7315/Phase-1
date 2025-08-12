#  3. Factorial of a number (no math.factorial)
def fact_of_number(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
