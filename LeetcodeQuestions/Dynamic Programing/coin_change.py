class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #  we will take a bottom up approach to solving this problem
        tab = [amount + 1] * amount + 1
        #  [0,12,12,12,12,12,12,12]
        #  [1,3,4,5]
        tab[0] = 0

        for i in range(1, len(tab)-1):
            for coin in coins:
                if tab[i] - coin >= 0:
                    tab[i] = min(tab[i], tab[i - coin])
        if tab[amount] == amount + 1:
            return -1
        else:
            return tab[amount]
