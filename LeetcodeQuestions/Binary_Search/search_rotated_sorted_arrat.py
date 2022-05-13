class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for idx, val in enumerate(nums):
            if val == target:
                return idx
        return -1
