class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        colum = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [[""] * n for i in range(n)]

        def Backtrack(r):
            if r == n:
                copy = ["".join(row) for row in range(r)]
                res.append(copy)
                return

            for c in range(n):

                if c in colum or (r + c) in posDiag or (r - c) in negDiag:
                    continue
