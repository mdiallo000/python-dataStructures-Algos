import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Input: grid = [
        #   ["1","1","1","1","0"],
        #   ["1","1","0","1","0"],
        #   ["1","1","0","0","0"],
        #   ["0","0","0","0","0"]
        # ]
        # Output: 1
        # Intuitively we want to identify the number of

        ROWS = len(grid)
        COLUMS = len(grid[0])

        def sink(r, c):

            if r < 0 or r == ROWS or c < 0 or c == COLUMS or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            sink(r+1, c)
            sink(r-1, c)
            sink(r, c+1)
            sink(r, c-1)

        islands = 0
        for r in range(ROWS):
            for c in range(COLUMS):
                if grid[r][c] == "1":
                    sink(r, c)
                    islands += 1
        return islands
