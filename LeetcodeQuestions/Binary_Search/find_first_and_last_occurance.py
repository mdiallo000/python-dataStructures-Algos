class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #  My initial working solution

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
        # this would solve the problem but its really not a log(n) time complexity since some edge cases will lead us to linearly scan even after we have found the midpoint

        # The best approach would be to use to binary searches. One to find the lower bound occurance and the other to find the upper bound.
