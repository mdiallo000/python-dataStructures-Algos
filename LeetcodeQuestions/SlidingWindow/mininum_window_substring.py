from collections import Counter
from operator import index


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window = {}
        countT = Counter(t)
        res, resLen = [-1, -1], float(-inf)
