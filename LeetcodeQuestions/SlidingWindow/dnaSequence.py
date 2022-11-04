class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        tmp = set()

        for r in range((len(s) + 9)):
            curr = s[r:r+10]

            if len(curr) < 10:
                break
