class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def dfs(idx, buying):
            if idx >= len(prices):
                return dp[(idx, buying)]
