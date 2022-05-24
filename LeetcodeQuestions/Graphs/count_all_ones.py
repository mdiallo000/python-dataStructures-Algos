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

        for r in range(rows):
            for c in range(colums):
                if grid[r][c] == 1:
                    count_ones =
