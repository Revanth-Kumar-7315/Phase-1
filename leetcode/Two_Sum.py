"""
🧩 1. Problem: Two Sum

Link: Two Sum – Easy
Goal: Given a list and a target, return indices of two numbers that add up to the target.
"""


def twoSum(nums, target):
    for i in range(len(nums)):
        j = i + 1
        for j in range(j, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # Return an empty list if no solution is found


# HashMap Solutiondef twoSumHashMap(nums, target):
"""   def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [i, seen[complement]]
            seen[num] = i """
