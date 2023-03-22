from collections import defaultdict


class Solution:

    def canBeTypedWord(self, text, brokenLetters):

        res = 0
        for w in text.split(" "):
            for c in w:
                if c in brokenLetters:
                    res -= 1
                    break
            res += 1
        return res
