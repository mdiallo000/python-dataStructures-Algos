

import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLUMS = len(grid), len(grid[0])
        time_count, fresh_orange = 0, 0
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
        while queue and fresh_orange > 0:

            for i in range(len(queue)):
                #  we pop out the coordinates of the current rotten oranges in the queue
                r, c = queue.popleft()
                #  we need to apply this algo in the 4 directions of the grid

                for dr, dc in directions:
                    row, colum = dr + r, dc + c
                    if row < 0 or colum < 0 or row == ROWS or colum == COLUMS or grid[row][colum] != 1:
                        continue
                    grid[row][colum] = 2
                    queue.append([row, colum])
                    fresh_orange -= 1
            time_count += 1

        return time_count if fresh_orange == 0 else -1
