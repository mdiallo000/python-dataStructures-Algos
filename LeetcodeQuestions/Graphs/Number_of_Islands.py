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

        row = len(grid)
        colum = len(grid[0])
        number_islands = 0

        def DFS(r, c):
            grid[r][c] = "*"
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in direction:
                next_dr, next_dc = r + dr, c + dc
                if 0 <= next_dr < row and 0 <= next_dc <= colum and grid[next_dr][next_dc] == '1':
                    DFS(next_dr, next_dc)

        for r in range(row):
            for c in range(colum):
                if grid[r][c] == "1":
                    DFS(r, c)
                    number_islands += 1
        return number_islands
