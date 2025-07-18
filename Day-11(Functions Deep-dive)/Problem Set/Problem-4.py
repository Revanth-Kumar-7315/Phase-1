# Use reduce() to find GCD of a list of numbers.
from functools import reduce


def gcd(a, b):
    return reduce(lambda x, y: x if y == 0 else gcd(y, x % y), [a, b])
