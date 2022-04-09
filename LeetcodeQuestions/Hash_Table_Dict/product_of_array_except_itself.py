# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        product_of_elems = 1
        for elem in nums:
            product_of_elems *= elem

        for elem in nums
        val = product_of_elems//elem
        arr.append(val)
