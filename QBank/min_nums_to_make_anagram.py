class Solution:
    def minSteps(self, s: str, t: str) -> int:

        DictS = {}, {}

        for char in s:
            if char not in DictS:
                DictS[char] = 1
            else:
                DictS[char] += 1
        changes = 0
        for char in t:
            if char in DictS and DictS[char] > 0:
                DictS[char] -= 1
            else:
                changes += 1
        return changes
