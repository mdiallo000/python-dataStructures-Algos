class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:

            m = (l+r - 1) // 2
