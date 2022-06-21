from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = defaultdict(set)
        colum = defaultdict(set)
        square = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
