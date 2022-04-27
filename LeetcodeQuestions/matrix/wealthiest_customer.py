

# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # so we need to take the sum of each customers bank balance. Each array inside of our 2d matrix represents a bank account

        for account in accounts:

            max_wealth = sum(account)
            wealthiest = 0
            wealthiest = max(max_wealth, )
