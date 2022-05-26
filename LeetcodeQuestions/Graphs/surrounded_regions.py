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
