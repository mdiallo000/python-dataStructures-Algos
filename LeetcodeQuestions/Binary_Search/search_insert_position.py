class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        #  we use regular binary search but instead of returning -1 if the target found, we instead return the L pointer
