class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS = len(grid2)
        COLUMNS = len(grid2[0])

        def dfs(r, c):

            if r == ROWS or r < 0
