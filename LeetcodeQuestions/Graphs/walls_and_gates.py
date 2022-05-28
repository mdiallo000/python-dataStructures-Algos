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
                if rooms[r][c] == 0:
                    queue.append([r, c])
                    visit.add((r, c))

        #  Now that we know exactly where the gates are we need to traverse the board and make sure we examine the exact grid that fits our criteria
        def addRoom(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLUMS or (r, c) in visit or rooms[r][c] == -1:
                return
            visit.add(r, c)
            queue.append([r, c])

        distance = 0

        while queue:
            length = len(queue)

            for i in range(length):
                r, c = queue.popleft()

                rooms[r][c] = distance
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            distance += 1
