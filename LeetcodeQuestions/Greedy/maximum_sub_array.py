class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSub = nums[0]

        curSum = 0

        for n in nums:
