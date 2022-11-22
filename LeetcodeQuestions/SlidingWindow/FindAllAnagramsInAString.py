class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        plen = len(p)

        if len(s) < len(p):
            return []

        pCount = Counter(p)
