from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        # Explanation:

        # the 2D grid is:

        # INF  -1  0  INF
        # INF INF INF  -1
        # INF  -1 INF  -1
        # 0  -1 INF INF

        # the answer is:
        # 3  -1   0   1
        # 2   2   1  -1
        # 1  -1   2  -1
        # 0  -1   3   4

        #  startting from the gates we can go and mark any subsquent open spot with the distance that is away from the gate
        ROWS, COLUMS = len(rooms), len(rooms[0])
        visit = set()
        queue = deque()

        #  we willl now go through the entire board and get the coordinates of our gates, so that we know where we need to start fro,
        for r in range(ROWS):
            for c in range(COLUMS):
