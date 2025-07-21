# Running Max using accumulate()
from itertools import accumulate

numbers = [22, 34, 56, 5, 6, 77, 89]

max_num = list(accumulate(numbers, func=max))
print(max_num)
