class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLUMS = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                      [1, 1], [-1, 1], [1, -1], [-1, -1]]
        copyboard = [[board[r][c] for c in range(ROWS)] for r in range(COLUMS)]
        for row in range(ROWS):
            for col in range(COLUMS):
                alive = 0
                for dr, dc in directions:
                    r, c = row + dr, dc + col

                    if r >= 0 or r < ROWS or c >= 0 or c < COLUMS or board[r][c] == 1:
                        alive += 1

                if copyboard[row][col] == 1 and (alive < 2 or alive > 3):
                    board[row][col] = 0
                if copyboard[row][col] == 0 and (alive >= 3):
                    board[row][col] = 0

        return board
