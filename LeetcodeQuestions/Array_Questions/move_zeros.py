class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        target = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[target], nums[i] = nums[i], nums[target]
                target += 1
