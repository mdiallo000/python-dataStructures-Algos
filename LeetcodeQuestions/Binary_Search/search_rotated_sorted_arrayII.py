class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #  problems states we are given an array that is sorted but its then rotated at a random pivot, our job is to return True if we find this target or false if its not found.

        #  easy but suboptimal solution is to do a linear scan and return the corresponding bool, this will be O(n) but we can do better but taking the fact that one side of the array must be sorted. we can have an log(n) solution:

        l, r = 0, len(nums)-1

        while l <= r:
            mid = r + l // 2

            if nums[mid] == target:
                return True
            # [4,5,6,7,0,1,2]
            #  l     m      r
            #  first case the leftmost elem is less than our mid
            if nums[l] <= nums[mid]:
                #  determine if target falls between a range
