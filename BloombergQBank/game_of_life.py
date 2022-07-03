class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLUMS = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                      [1, 1], [-1, 1], [1, -1], [-1, -1]]

        for r in range(ROWS)
        for c in range(COLUMS)
