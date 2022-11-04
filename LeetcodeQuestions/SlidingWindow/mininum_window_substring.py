class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ''
        index1, index2 = 0, 0
