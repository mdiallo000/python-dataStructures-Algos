class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    # Get the dimensions of the board we are working with
        ROWS, COLUMS = len(board), len(board[0])

    #  Now we will write the Traversal algorithm that will
        def Traverse(r, c):
