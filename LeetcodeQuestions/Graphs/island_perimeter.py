class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        Rows = len(grid)
        Columns = len(grid[0])
        visited = set()
