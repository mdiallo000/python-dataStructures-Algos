# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# list3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
#          l                       R
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, k in enumerate(nums, start=0):
            for i2, k2 in enumerate(nums[i+1:], start=0):
                if k + k2 == target:
                    return i, i2


class Answer:
    def TwoSumDict(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
