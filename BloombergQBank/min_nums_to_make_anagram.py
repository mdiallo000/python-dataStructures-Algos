class Solution:
    def minSteps(self, s: str, t: str) -> int:

        DictT, DictS = {}, {}

        for char in s:
            if char not in DictS:
                DictS[char] = 1
            else:
                DictS[char] += 1

        for char in s:
            if char not in DictT:
                DictT[char] = 1
            else:
                DictT[char] += 1
