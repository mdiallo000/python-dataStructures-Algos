class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLUMS = len(ROWS), len(COLUMS)
        time_count, fresh = 0, 0
        # def traverse(r,c):
