class UnionFind:

    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        for r in range(ROWS):
