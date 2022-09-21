class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        count = 0
        if len(nums) == 1:
            return 1
        for i in range(1, len(nums)):
