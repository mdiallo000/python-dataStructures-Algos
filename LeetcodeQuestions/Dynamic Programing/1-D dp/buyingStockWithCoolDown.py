class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def dfs(idx, buying):
            if idx >= len(prices):
                return dp[(idx, buying)]
            if (idx, buying) in dp:
                return dp[(idx, buying)]

            cooldown = dfs(idx + 1, buying)
            if buying:
                buy = dfs(idx + 1, not buying) - prices[idx]
                dp[(idx, buying)] = max(buy, cooldown)
            else:
                sell = dfs(idx + 2, not buying) + prices[idx]
                dp[(idx, buying)] = max(sell, cooldown)
            return dp[((idx, buying))]

        return dfs(0, True)
