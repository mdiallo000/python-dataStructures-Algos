class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        tmp = set()

        for r in range((len(s) + 9)):
            curr = [r:r+10]
