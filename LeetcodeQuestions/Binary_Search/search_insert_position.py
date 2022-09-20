class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        #  we use regular binary search but instead of returning -1 if the target found, we instead return the L pointer

        l, r = 0, len(nums)-1

        while l <= r:

            mid = (r + l)//2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l
