class Solution:
    #  The ultimate goal is to use O(1) extra space
    #  If this requirement didnt exist then we could simply use a set and filter out the duplicate values
    def removeDuplicates(self, nums: List[int]) -> int:

        for j in range(1, len(nums)):
