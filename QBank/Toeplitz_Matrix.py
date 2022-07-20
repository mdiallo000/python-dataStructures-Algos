class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        ROWS = len(matrix)
        COLUMS = len(matrix[0])

        if ROWS < 2 and COLUMS < 2:
            return True

        for r in range(ROWS - 1):
            for c in range(COLUMS - 1):
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False

        return True
