from collections import defaultdict

#  This problem is not very difficult to do
#  Intution: The entire goal is to determine if their are any duplicates in any row, column or in a 3*3 square

#  Strategy:
#  we can use a hash table. The key will be a particular row, or column or 3 by 3 square. The values will be a set that will help us determine whether or not we have encountered any duplicates


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
                row[r].add(board[r][c])
                colum[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True
