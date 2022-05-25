import collections
from msilib.schema import Complus


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, colums = len(heights), len(heights[0])
        v_atlantic = set()
        v_pacific = set()

        def DFS(visited, r, c, prev_values):
            # we first need to chech wheter our current location is out of bounds or not
            if r < 0 or r >= rows or c < 0 or c >= colums or (r, c) in visited or prev_values > grid[r][c]:
                return
            #  If these conditions are not met than we can add them to our visited set
            visited.add((r, c))
            # now we run our traversal function on every direction from north, east, west, south for the current position we are on
            DFS(visited, r + 1, c, prev_values)
            DFS(visited, r - 1, c, prev_values)
            DFS(visited, r, c+1, prev_values)
            DFS(visited, r, c-1, prev_values)

        for c in range(colums):
            # for top of the top(pacific) and bottom(atlantic)
            DFS(v_pacific, 0, colums, heights[0][colums])
            DFS(v_atlantic, rows-1, colums, heights[rows-1][colums])

        for r in range(rows):
            # left(pacific) and right (atlantic)
            DFS(v_pacific, rows, 0, heights[rows][0])
            DFS(v_atlantic, rows, colums-1, heights[rows][colums-1])
        res = v_atlantic.intersection(v_pacific)

        return res
