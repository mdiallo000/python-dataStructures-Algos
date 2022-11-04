from collections import Counter
from operator import index


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window = {}
        countT = Counter(t)
        res, resLen = [-1, -1], float(-inf)
        have, need, l = 0, len(countT), 0
        for r in range(len(s)):
            char = s[r]
            #  we add this current character into our window
            window[char] = 1 + window.get(char, 0)
            #  after we have added the character we now look to see if we can update our have
            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:

                if (r + l - 1) < resLen:
                    res = [l, r]
                    resLen = (r + l - 1)

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        return res[l:r+1] if resLen != float(-inf) else ""
