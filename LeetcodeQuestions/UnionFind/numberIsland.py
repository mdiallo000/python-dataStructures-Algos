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
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1
