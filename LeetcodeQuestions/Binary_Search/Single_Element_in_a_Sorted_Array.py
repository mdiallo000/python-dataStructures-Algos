class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #  You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

        # Return the single element that appears only once.

        # Your solution must run in O(log n) time and O(1) space

        l, r = 0, len(nums)-1

        # while l != r:

        #     if nums[l] == nums[l +1]:
        #         l +=2
        #     if nums[r] == nums[r-1]:
        #         r -=2
        # return l
        #  the solution above is not logorithmic in nature, but it is more efficient than a simple linear scan used with extra space
