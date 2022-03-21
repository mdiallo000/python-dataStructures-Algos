# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# list3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
#          l                       R
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, elm in enumerate(nums):
            for idx2, elm2 in enumerate(nums[idx+1]):
                if elm + elm2 == target:
                    return (idx, idx2+idx+1)

class Answer:
    def TwoSumDict(self, nums:List[int],target:int) -> List[int]:
        myDict = {}
            