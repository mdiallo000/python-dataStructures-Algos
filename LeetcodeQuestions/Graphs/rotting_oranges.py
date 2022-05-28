

import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLUMS = len(ROWS), len(COLUMS)
        time_count, fresh = 0, 0
        queue = collections.deque()

        #  We will loop through the entire grid to check how many fresh oranges we have as well ass add the rotten oranges to our queue
        for r in range(ROWS):
            for c in range(COLUMS):
                if grid[r][c] == 2:
                    queue.append([r, c])
                if grid[r][c] == 1:
                    fresh_orange += 1

        # now that we know how many fresh oranges we have we can tell wheter or not we managed to rotten all the oranges
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh == 0:

            for i in range(len(queue)):
                #  we need to apply this algo in the 4 directions of the grid
