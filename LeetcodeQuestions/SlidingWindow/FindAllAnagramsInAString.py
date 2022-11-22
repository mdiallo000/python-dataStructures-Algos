class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        plen = len(p)

        if len(s) < len(p):
            return []

        pCount = Counter(p)
        window = defaultdict(0)

        for r in range(len(s)):
