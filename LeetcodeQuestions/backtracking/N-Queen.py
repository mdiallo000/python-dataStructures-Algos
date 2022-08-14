class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        colum = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for i in range(n)]

        def Backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):

                if c in colum or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                colum.add(c)
                posDiag.add(r + c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                Backtrack(c + 1)
                colum.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r-c)
                board[r][c] = "."
        Backtrack(0)
        return res
