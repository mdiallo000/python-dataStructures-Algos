class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ''
        index1, index2 = 0, 0
        res = ""
        currMin = float(inf)
        while index1 < len(s):
