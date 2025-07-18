# Write a recursive function to calculate the sum of digits of a number.
def sum_of_digits(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    else:
        # Recursive case: return the last digit plus the sum of the remaining digits
        return n % 10 + sum_of_digits(n // 10)
