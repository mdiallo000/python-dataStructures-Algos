# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter = {}

        for char in s1:
            s1Counter[char] = 1 + s1Counter.get(char, 0)

        l = 0
        r = 1
        while r < len(s2)-1:
