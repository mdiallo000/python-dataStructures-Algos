# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

class Solution:
    def maxProfitBruteForce(self, prices: List[int]) -> int:
        maxprofit = 0
        profit_that_day = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit_that_day = j - i
                maxprofit = max(maxprofit, profit_that_day)
        return maxprofit

    def maxProfit(self, prices: List[int]) -> int:
