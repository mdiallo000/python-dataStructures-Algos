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

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid2[r][c] == 1 and grid1[r][c] == 0:
                    dfs(r, c)
        res = 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid2[r][c] == 1:
                    dfs(r, c)
                    res += 1
        return res
