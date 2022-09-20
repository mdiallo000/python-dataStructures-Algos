class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #  My intial woprking solution

        l, r = 0, len(nums)-1

        while l <= r:
            mid = r + l // 2

            if target == nums[mid]:
                while nums[l] != target:
                    l += 1
