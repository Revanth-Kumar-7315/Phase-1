class Solution:
    def removeDuplicates(nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        k = i + 1
        return k
