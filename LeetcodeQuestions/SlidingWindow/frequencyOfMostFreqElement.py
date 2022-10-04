class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        currMax = 0
        l, r = 0, 0
        while l <= r:
