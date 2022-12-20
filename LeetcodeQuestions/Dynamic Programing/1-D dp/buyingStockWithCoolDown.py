class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def dfs(idx, buying):
            if idx >= len(prices):
                return 0
            #  if we go out of bounds then there is nothing to be bought and thus we must return zero

            if (idx, buying) in dp:
                return dp[(idx, buying)]
            #  if this day and state has been previously seen then we should just return the already cached values.
            cooldown = dfs(idx + 1, buying)
            if buying:
                buy = dfs(idx + 1, not buying) - prices[idx]
                dp[(idx, buying)] = max(buy, cooldown)
            else:
                sell = dfs(idx + 2, not buying) + prices[idx]
                dp[(idx, buying)] = max(sell, cooldown)
            return dp[((idx, buying))]

        return dfs(0, True)
