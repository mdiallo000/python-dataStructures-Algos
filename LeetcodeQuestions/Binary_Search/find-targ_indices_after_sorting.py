# You are given a 0-indexed integer array nums and a target element target.
# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
#  test case : [1,2,1,2,3,4,5] target  = 2
#  result : [1,3]
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        nums.sort()
        for idx, value in enumerate(nums):
            if value == target:
                result.append(idx)
        return result
        # above is a working linear seach algorithm approach with a time complexity of O(n)
        # we can do better with  Binary search
