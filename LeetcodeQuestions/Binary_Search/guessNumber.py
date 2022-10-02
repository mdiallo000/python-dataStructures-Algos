class Solution:
    def guessNumber(self, n: int) -> int:

        l, r = 1, n
        while l <= r:
            mid = r + l // 2
            ans = guess(mid)
            if ans > 0:
                mid = l + 1
            elif ans < 0:
                r = mid - 1
            else:
                return mid
