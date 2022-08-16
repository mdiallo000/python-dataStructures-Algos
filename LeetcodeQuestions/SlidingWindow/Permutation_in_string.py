# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2) or len(s1) == 0:
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[2] else 0)
        l = 0
        for r in range(len(s1), len(s2)):

            if matches == 26:
                return True

            position = ord(s2[r]) - ord('a')
            s2Count[position] += 1
            if s1Count[position] == s2Count[position]:
                matches += 1
            elif s1Count[position] + 1 == s2Count[position]:
                matches += 1

            position = ord(s2[l]) - ord('a')
            s2Count[position] -= 1
            if s1Count[position] == s2Count[position]:
                matches += 1
            elif s1Count[position] - 1 == s2Count[position]:
                matches -= 1
