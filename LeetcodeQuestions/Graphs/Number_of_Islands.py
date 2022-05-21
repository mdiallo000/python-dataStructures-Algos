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
        island = 0
        visited = set()

        for r in range(row):
            for c in range(colum):
                if grid[r][c] == "1" and r and c not in visited:
