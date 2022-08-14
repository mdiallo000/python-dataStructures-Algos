class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l, r = 0, 0
        res = 0
        count = 0
        total = 0

        while r < len(nums):
            total += nums[r]
            if total < target:
                r += 1
            else:
                res = min(res, r - l + 1)
