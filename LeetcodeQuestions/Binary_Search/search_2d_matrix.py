
# Input: matrix = [
# Rows[1,3,5,7],
#    [10,11,16,20],
#    [23,30,34,60]
# # # ]


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_pos = 0
        colum_pos = len(matrix[0]) - 1
# we will run a while loop as long as our collumn is greater than 0 since we always started from the farthest point of our matrix. On the other hand we need to make sure our row doesnt exceed the lenght of our matrix since we will move down the matrix.
#  Collum moves across to the left
#  Row moves down.
        while colum_pos >= 0 and row_pos <= len(matrix) - 1:

            if matrix[row_pos][colum_pos] < target:
                row_pos += 1

            elif matrix[row_pos][colum_pos] > target:
                colum_pos -= 1

            else:
                return True

        return False


#         row_size = 0
#         col_size = len(matrix[0]) - 1

#         while(col_size >= 0 and row_size <= len(matrix)-1):
#             if matrix[row_size][col_size] < target:
#                 row_size += 1
#
#             elif matrix[row_size][col_size] > target:
#                 col_size -= 1

#             else:
#                 return True

#         return False
