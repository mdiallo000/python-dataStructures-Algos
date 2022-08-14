class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l, r = 0, 0
        res = 0
        count = 0

        while r < len(nums):
