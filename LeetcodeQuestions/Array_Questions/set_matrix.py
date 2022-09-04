class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        RowSet = set()
        ColumnSet = set()
        row = len(matrix)
        column = len(matrix[0])

        for r in range(row):
            for c in range(column):
                if matrix[r][c] == 0:
                    RowSet.add(r)
                    ColumnSet.add(c)

        for r in range(row):
            for c in range(column):
                if r in RowSet or c in ColumnSet:
                    matrix[r][c] = 0
        #  this was my initial appraoch and intuition, but i am certain that their are more efficient ways of doing it with better time complexity
