class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        plen = len(p)

        if len(s) < len(p):
            return []

        pCount = Counter(p)
        window = defaultdict(int)
        res = []
        for r in range(len(s)):
            #  i need to add each char into my window
            window[s[r]] += 1
            if r >= plen:

                if window[s[r - plen]] == 1:
                    del window[s[r - plen]]
                else:
                    window[s[r - plen]] -= 1
                    #  we know when the window and pCount are the same then we can return
            if window == pCount:
                res.append(r - plen + 1)
        return res
