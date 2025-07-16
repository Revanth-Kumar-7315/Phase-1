def majorityElement(nums):
    number_counter = {}
    for i in nums:
        number_counter[i] = number_counter.get(i, 0) + 1
        for num, count in number_counter.items():
            if count > len(nums) // 2:
                return num
