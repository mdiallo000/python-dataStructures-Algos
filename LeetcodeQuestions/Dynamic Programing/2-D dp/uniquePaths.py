class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        row = [1] * m

        for _ in range(m - 1):
            newRow = [1] * m
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row
