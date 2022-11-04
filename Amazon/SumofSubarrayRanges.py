class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        #  the brute force way is to just use two for loops
        res = 0
        for left in range(len(nums)):
            for right in range(left, len(nums)):
