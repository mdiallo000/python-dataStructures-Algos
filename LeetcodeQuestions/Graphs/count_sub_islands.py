class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS = len(grid2)
        COLUMNS = len(grid2[0])

        def dfs(r, c):

            if r == ROWS or r < 0 or grid2[r][c] == 0 or c < 0 or c == COLUMNS:
                return
            grid2[r][c] == 0
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
