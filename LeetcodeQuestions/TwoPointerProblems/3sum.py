
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resulting_arr = []
        # Sort the array and now we can apply the same technique we used in 2sumTwo
        nums.sort()
#
        for index, curr in enummerate(nums):
