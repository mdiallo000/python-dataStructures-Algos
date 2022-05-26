from tkinter.tix import ROW


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    # Get the dimensions of the board we are working with
        ROWS, COLUMS = len(board), len(board[0])

    #  Now we will write the Traversal algorithm that will
        def Traverse(r, c):
            #  this base case will return once we no longer me the conditions
            if 0 < r >= ROWS or 0 < c >= COLUMS or board[r][c] != "O":
                return
            board[r][c] = "T"
            Traverse(r+1, c)
            Traverse(r-1, c)
            Traverse(r, c+1)
            Traverse(r, c-1)
    #  Now we run this traversal algo on the edges of our board to change the unsorrounded O into another char
        for r in range(ROWS):
            for c in range(COLUMS):
                if board[r][c] == "O" and (r in [0, ROWS - 1]) and (c in [0, COLUMS - 1]):
                    Traverse(r, c)

                #  NOW ALL OF THE O NEXT TO THE BORDER OF THE BOARD WILL CHANGE INTO ANOTHER CHAR

    #  The Next step is change the surronded O's in to X's
        for r in range(ROWS):
            for c in range(COLUMS):
                if board[r][c] == "O":
                    board[r][c] = "x"

    #  Finally we change the T's back to X's
        for r in range(ROWS):
            for c in range(COLUMS):
                if board[r][c] == "T":
                    board[r][r] = "O"
