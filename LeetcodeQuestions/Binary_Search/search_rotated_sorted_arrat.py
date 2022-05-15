from tkinter import W


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2] tar = 0
        # [1,2,3,4,5,6]
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid

            # NOW WE chech whether or not does our target value falls bettwen the boundaris of l<= targ <= mid

            if nums[l] < nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    #  in other words our target falls into the left sorted portion
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target <= nums[r] and target >= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
