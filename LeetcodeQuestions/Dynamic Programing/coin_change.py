class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #  we will take a bottom up approach to solving this problem
        tab = [amount + 1] * amount + 1

        tab[0] = 0

        for i in range(1, len(tab)-1):
