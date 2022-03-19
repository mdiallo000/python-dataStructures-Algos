class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        for i in range(0, len(nums)):
            if i not in nums:
                return i
