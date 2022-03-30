# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in nums:
            left = i+1
            right = len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums
