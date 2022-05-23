class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # grid =
        # [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

        row = len(grid)
        colum = len(grid[0])
        number_islands = 0
        visited = set()

        def DFS(r, c):
            if (r < 0 or r == row or c < 0 or c == colum or grid[r][c] != 1 or (r, c) in visited):
                return 0
            visited.add((r, c))
            return (1 + DFS(r + 1, c) + DFS(r - 1, c) + DFS(r, c+1) + DFS(r, c-1))

        for r in range(row):
            for c in range(colum):
                number_islands = max(number_islands, DFS(r, c))
        return number_islands
