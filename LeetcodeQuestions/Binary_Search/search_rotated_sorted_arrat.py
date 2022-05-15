from tkinter import W


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2,3] tar = 0

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
