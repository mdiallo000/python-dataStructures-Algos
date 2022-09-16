class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):

            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
        # Time complexity for this solution is O(n) and constant space

    #  Intuition
