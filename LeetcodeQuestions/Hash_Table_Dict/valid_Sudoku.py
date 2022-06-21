from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = defaultdict(set)
        colum = defaultdict(set)
        square = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                #  if the value at this current cell is not a number then we will skip it
                if board[r][c] == ".":
                    continue
                # next we check if this current cell is already been found in our rows, colum or square

                if (board[r][c] in row[r] or board[r][c] in colum[c] or board[r][c] in square[(r//3, c//3)]):
                    #  we will return false since this is not a valid sudoku anymore
                    return False
