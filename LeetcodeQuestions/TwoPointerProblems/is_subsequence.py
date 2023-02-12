# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        # We can use two pointers travel the le
        if len(s) > len(t):
            return False

        i, j = 0, 0
        while j < len(t):
            if t[j] == s[i]:
                i += 1
                j += 1
                if i > len(s)-1:
                    return True
            else:
                j += 1
        return False
