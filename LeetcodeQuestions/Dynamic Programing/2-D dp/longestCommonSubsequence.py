class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_table = [[0 for i in range(len(text2) + 1)]
                    for i in range(len(text1) + 1)]
