# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result
