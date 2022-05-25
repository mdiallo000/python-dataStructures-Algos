import collections
from msilib.schema import Complus


class Solution:

    # rows, colums = len(heights), len(heights[0])
    # v_atlantic = set()
    # v_pacific = set()

    # def DFS(visited, r, c, prev_values):
    #     # we first need to chech wheter our current location is out of bounds or not
    #     if r < 0 or r >= rows or c < 0 or c >= colums or (r, c) in visited or prev_values > grid[r][c]:
    #         return
    #     #  If these conditions are not met than we can add them to our visited set
    #     visited.add((r, c))
    #     # now we run our traversal function on every direction from north, east, west, south for the current position we are on
    #     DFS(visited, r + 1, c, prev_values)
    #     DFS(visited, r - 1, c, prev_values)
    #     DFS(visited, r, c+1, prev_values)
    #     DFS(visited, r, c-1, prev_values)

    # for c in range(colums):
    #     # for top of the top(pacific) and bottom(atlantic)
    #     DFS(v_pacific, 0, colums, heights[0][colums])
    #     DFS(v_atlantic, rows-1, colums, heights[rows-1][colums])

    # for r in range(rows):
    #     # left(pacific) and right (atlantic)
    #     DFS(v_pacific, rows, 0, heights[rows][0])
    #     DFS(v_atlantic, rows, colums-1, heights[rows][colums-1])
    # res = v_atlantic.intersection(v_pacific)

    # return res
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, colums = len(heights), len(heights[0])
        v_pac = set()
        v_atl = set()

        def dfs(v_set, row, col, curr_height):
            if row < 0 or row >= rows or \
                    col < 0 or col >= colums or \
                (row, col) in v_set or \
                    curr_height > heights[row][col]:
                return
            v_set.add((row, col))

            curr_height = heights[row][col]
            dfs(v_set, row + 1, col, curr_height)
            dfs(v_set, row - 1, col, curr_height)
            dfs(v_set, row, col + 1, curr_height)
            dfs(v_set, row, col - 1, curr_height)

        # Approach is to start from both sides of
        # the oceans and then reach each point that can be
        # reached while maintaining the visited indices

        # Iterate over columns and start from both 0, m-1 rows
        for col in range(colums):
            dfs(v_pac, 0, col, heights[0][col])  # First row
            dfs(v_atl, row - 1, col, heights[row-1][col])  # Last row

        # Iterate over rows and start from both 0, n-1 cols
        for row in range(row):
            dfs(v_pac, row, 0, heights[row][0])  # First column
            dfs(v_atl, row, colums-1, heights[row][colums-1])  # Last column

        # Co-ordinates which can reach both the oceans are the winners
        # so we take intersection
        result = v_atl.intersection(v_pac)

        return result
