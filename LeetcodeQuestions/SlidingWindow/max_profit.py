class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  we are given stocks to buy and sell
        #  the rules are simple, our goal is to maximize our profits, we can do so by buying low and selling high
        #  we can easily come up with a naive solution where we see how much profit can be made by buy on each day and then selling on every subsequent day
        # This would yield an O(n^2) algorithm
        # max_profit = 0
        # for today in range(len(prices)):
        #     for future in range(today, len(prices)):
        #         max_profit =  max(max_profit, (prices[future] - prices[today]))
        # return max_profit

        #  We can create a linear algorithm by applying the sliding window techinque were we only examine the window where we are generating profit and whenever we encouter a new low price we take that as our new starting point
        today, future = 0, 0
        max_profit = 0
        while future < len(prices):
            if prices[future] < prices[today]:
                today = future
            max_profit = max(max_profit, (prices[future] - prices[today]))
            future += 1

        return max_profit

        #  with this technique we manage to effieciently finds the higest profit margin possible
