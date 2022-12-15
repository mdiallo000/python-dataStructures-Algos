class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_table = [[0 for j in range(len(text2) + 1)]
                    for i in range(len(text1) + 1)]
        for row in range(len(text1)-1, -1, -1):
            for col in range(len(text2) - 1, -1, - 1):
                #  we are only interested in two conditions
                #  1 if the two charaters at this position matches for both words than the value will be 1 + whatever we found diagonally
                if text1[row] == text2[col]:
                    dp_table[row][col] = 1 + dp_table[row+1][col+1]
                else:
                    dp_table[row][col] = max(
                        dp_table[row+1][col], dp_table[row][col+1])
        return dp_table[0][0]
