class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        self.memo = {}

        return self.rob_from(0, nums)

    def rob_from(self, idx, houses):
        #  establish base case, which will be if we run out of houses

        if idx >= len(houses):
            return 0

        if idx in self.memo:
            return self.memo[idx]

        ans = max(self.rob_from(idx + 1, houses), self.rob_from(idx+2, houses) + houses[idx])

        self.memo[idx] = ans
        return ans
