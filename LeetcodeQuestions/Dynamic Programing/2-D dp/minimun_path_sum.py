class Solution:
    #  this is a typical dp problem, we need to find the path withing the grid that we generate the minimum sum
    #  the constraint we have is that we can only travel from the top to left to the bottom right corner of the grid
    #
    def minPath(grid):
        row, column = len(grid), len(grid[0])
        dp = [[0] * column for _ in range(row)]
        dp[0][0] = grid[0][0]
