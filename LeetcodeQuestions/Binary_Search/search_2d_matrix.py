class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_size = len(matrix[0]) - 1
        col_size = 0

        while(row_size > 0 and col_size < len(matrix)):
            if matrix[row_size][col_size] < target:
                row_size -= 1

            elif matrix[row_size][col_size] > target:
                col_size += 1
            else:
                return True

        return False
