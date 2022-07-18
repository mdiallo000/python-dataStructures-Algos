class Solution:
    def customSortString(self, order: str, s: str) -> str:

        count = Counter(s)
        ans = []
        # "cbad"
        #  i
        for char in order:
            ans.append(char * count[char])
            count[char] = 0
        for char in count:
            ans.append(char * count[char])

        res = ''.join(ans)
        return res
