class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        lis = [1] * len(nums)

        for i in range(len(s)-1, -1, -1):
