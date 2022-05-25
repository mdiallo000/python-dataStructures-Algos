import collections


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
