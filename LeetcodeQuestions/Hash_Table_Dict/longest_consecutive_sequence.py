# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

from msilib import sequence


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        sequence = 0
        for number in nums:
            if (number-1) not in myset:
                longest = 0
                while (number + 1) in myset:
                    longest += 1
                sequence = (longest, longest)
        return sequence
