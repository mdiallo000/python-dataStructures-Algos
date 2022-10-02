class Solution:
    def guessNumber(self, n: int) -> int:

        nums = [i for i in range(1, n+1)]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = r + l // 2
            curr = nums[mid]
            ans = guess(curr)
            if ans > 0:
                mid = l + 1
            elif ans < 0:
                r = mid - 1
            else:
                return curr
