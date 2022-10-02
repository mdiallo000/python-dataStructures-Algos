class Solution:
    def guessNumber(self, n: int) -> int:

        nums = [i for i in range(1, n+1)]
        l, r = 0, len(nums)-1
