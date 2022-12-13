class UnionFind:

    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == "1":
                    self.parent.append(r * COLUMNS + c)
                    count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, )
