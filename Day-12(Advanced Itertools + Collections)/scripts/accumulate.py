from itertools import accumulate

numbers = [1, 2, 3, 4, 5]
running_sum = accumulate(numbers)
print(list(running_sum))
