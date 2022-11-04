class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        #  the brute force way is to just use two for loops
        res = 0
        for left in range(len(nums)):
            minV, maxV = float(-inf), float(inf)
            for right in range(left, len(nums)):
                minV = min(minV, nums[right])
                maxV = max(maxV, nums[right])
                res += abs(minV - maxV)
        return res
