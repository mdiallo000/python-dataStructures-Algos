class Solutions:

    def countAllOneMatrix(self, grid: List[List[str]]):

        #  [
        #      [1,1,0,0,0],
        #      [0,1,0,1,0],
        #      [0,1,1,1,0],
        #      [0,1,0,0,0]
        # ]
        rows = len(grid)
        colums = len(grid[0])
        count_ones = 0

        def dfs(r, c):
            grid[r][c] = "*"
            directions = [[1, 0], [-1, 0], [0, 1], [0-1]]

            for x, y in directions:
                dr, dc = r + x, c + y
                if 0 <= dr < rows and 0 <= dc < colums and grid[dr][dc] == 1:
                    dfs(dr, dc)

        for r in range(rows):
            for c in range(colums):
                if grid[r][c] == 1:
                    dfs(r, c)
                    count_ones += 1
