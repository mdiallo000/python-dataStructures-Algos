class Solution:

    def minPath(grid):
        row, column = len(grid), len(grid[0])
        dp = [[0] * column for _ in range(row)]
        dp[0][0] = grid[0][0]
