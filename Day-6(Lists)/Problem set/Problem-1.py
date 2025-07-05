# Return sum of all even numbers in a list
def sum_evens(lst):
    sum_of_even = 0
    for i in lst:
        if i % 2 == 0:
            sum_of_even += i
    return sum_of_even
