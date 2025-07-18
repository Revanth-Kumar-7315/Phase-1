# Use reduce() to find the product of all elements in a list.
def product_of_list(numbers):
    from functools import reduce

    return reduce(lambda x, y: x * y, numbers)
