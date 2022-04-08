# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l, r = 0, 1

        while r <= len(s2):
            if s2[l] and s2[r] in s1:
                return True
            else:
                l, r += 1
        return False
