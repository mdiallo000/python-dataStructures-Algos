class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l < r:

            mid = l + (r - l)//2
