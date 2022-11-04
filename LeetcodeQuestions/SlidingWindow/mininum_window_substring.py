from operator import index


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ''
        index1, index2 = 0, 0
        res = ""
        currMin = float(inf)
        while index1 < len(s):

            if s[index1] == t[index2]:
                index2 += 1

                if index2 == len(t):
                    start, end = index1, index1 + 1
