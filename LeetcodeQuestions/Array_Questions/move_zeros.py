class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        target = 0

        for i in range(len(nums)):

            if nums[i] != 0:
