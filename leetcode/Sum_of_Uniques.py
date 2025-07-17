def sumOfUnique(nums):
    freq_map = {}
    sum = 0
    for i in nums:
        freq_map[i] = freq_map.get(i, 0) + 1
    for i in freq_map:
        if freq_map[i] == 1:
            sum += i
    return sum
