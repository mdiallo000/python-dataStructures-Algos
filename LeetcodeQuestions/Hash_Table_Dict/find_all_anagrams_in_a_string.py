from collections import Counter, defaultdict
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        plen = len(p)

        if len(s) < len(p):
            return []

        pCount = Counter(p)
        window = defaultdict(int)
        res = []
        for r in range(len(s)):
            #  i need to add each char into my window
            window[s[r]] += 1
            if r >= plen:

                if window[s[r - plen]] == 1:
                    del window[s[r - plen]]
                else:
                    window[s[r - plen]] -= 1
                    #  we know when the window and pCount are the same then we can return
            if window == pCount:
                res.append(r - plen + 1)
        return res
