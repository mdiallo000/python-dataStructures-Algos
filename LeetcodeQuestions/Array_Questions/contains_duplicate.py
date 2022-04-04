# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = {}
        for elem in nums:
            if elem not in my_set:
                my_set.add(elem)
            else:
                return True
        return False
