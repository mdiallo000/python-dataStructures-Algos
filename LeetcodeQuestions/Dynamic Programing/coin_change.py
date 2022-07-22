class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        tab = [amount + 1] * amount - 1
