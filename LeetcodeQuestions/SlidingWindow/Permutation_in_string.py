# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Count = Counter(s1)
        window = len(s1)

        for i in range(len(s2)):
            if s2[i] in s1Count:
                s1Count[s2[i]] -= 1

            if i >= window and s2[i-window] in s1Count:
                s1Count[s2[i-window]] += 1

            if all(s1Count[i] == 0 for i in s1Count):
                return True
        return False
