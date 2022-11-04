from collections import Counter
from operator import index


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window = {}
        countT = Counter(t)
        res, resLen = [-1, -1], float(-inf)
        have, need = 0, len(countT)
        for r in range(len(s)):
            char = s[r]
            #  we add this current character into our window
            window[char] = 1 + window.get(char, 0)
            #  after we have added the character we now look to see if we can update our have
            if char in countT and window[char] == countT[char]:
                have += 1
