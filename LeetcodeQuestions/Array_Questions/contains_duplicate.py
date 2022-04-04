# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for elem in nums:
            if elem not in my_set:
                my_set.add(elem)
            else:
                return True
        return False

    def using_hashmap(self, nums: List[int]) -> bool:
        hash_map = {}

        for elem in nums:
            if elem not in hash_map:
                hash_map[elem] = 1
            else:
                hash_map[elem] += 1

        for key in hash_map:
            if hash_map[key] > 1:
                return True
        return False

    def brute_force(self, nums: List[int]) -> bool:

        for i in range(len(nums)-1):
            elem = nums[i]
            for j in range(i+1, len(nums)):
                if elem == nums[j]:
                    return True
        return False
