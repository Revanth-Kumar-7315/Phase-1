# 5. Sum of digits of a number
def sum_of_digits(n):
    sum_of_digits = 0
    while n > 0:
        last_digit = n % 10
        sum_of_digits += last_digit
        n //= 10
    return sum_of_digits
