class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #  My intial woprking solution

        l, r = 0, len(nums)-1

        while l <= r:
            mid = r + l // 2

            if target == nums[mid]:
                while nums[l] != target:
                    l += 1
                while nums[r] != target:
                    r -= 1
                return [l, r]
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return [-1, -1]
