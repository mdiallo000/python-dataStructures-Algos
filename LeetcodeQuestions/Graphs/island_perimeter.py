class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        Rows = len(grid)
        Columns = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r >= Rows or c >= Columns or r < 0 or c < 0 or grid[r][c] == 0:
                return 1

            if (r, c) in visited:
                return 0
            visited.add((r, c))

            res = dfs(r, c+1)
            res += dfs(r+1, c)
            res += dfs(r, c-1)
            res += dfs(r-1, c)
            return res
        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == 1:
                    return dfs(r, c)
# Intuition is to treat the borders and the empty cells (water) as a way of determining whether the border exists or not...So if a cell is adjacent to water or the board return 1 else if we already seen this cell return o
