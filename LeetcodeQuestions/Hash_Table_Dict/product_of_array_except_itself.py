# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
