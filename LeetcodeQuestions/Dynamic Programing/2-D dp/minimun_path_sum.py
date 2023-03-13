class Solution:
    #  this is a typical dp problem, we need to find the path withing the grid that we generate the minimum sum
    #  the constraint we have is that we can only travel from the top left to the bottom right corner of the grid
    # that means we can solve the problem efficiently by using dynamic programming
    #  for each cell we can determine the min cost to reach it by comparing the top and left cell values and adding those to the number in the current cell
    def minPath(grid):
        row, column = len(grid), len(grid[0])
        dp = [[0] * column for _ in range(row)]
        dp[0][0] = grid[0][0]
        #  here we prefill the top row by adding start at 1 and adding the value in the left cell plus the value at the current cell
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(column):
            dp[0][j] = dp[0][j-1] + grid[0][j-1]
