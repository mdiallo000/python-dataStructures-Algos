class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        Rows = len(grid)
        Columns = len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            if r >= Rows or c >= Columns or r < 0 or c < 0 or grid[r][c] == 0:
                return 1

            if (r, c) in visited:
                return 0
