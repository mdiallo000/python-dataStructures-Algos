class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l, r = 0, 0
        res = float('inf')
        count = 0
        total = 0

        while r < len(nums):
            total += nums[r]
            if total < target:
                r += 1
            else:
                res = min(res, r - l + 1)
                total = total - nums[l] - nums[r]
                l += 1
        return res if res < float('inf') else 0
