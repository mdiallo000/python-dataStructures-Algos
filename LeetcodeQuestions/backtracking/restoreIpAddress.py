class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res

        def backtrack(idx, dots, currIP):

            if dots == 4 or idx == len(s):
                res.append(currIP[:-1])
                return
            if dots > 4:
                return

            for j in range(idx, min(idx + 3, len(s))):
                if int(s[idx: j+1]) < 256 and (idx == j or s[idx] != "0"):
                    backtrack(idx, dots + 1, currIP + s[idx: j+1]+".")
        return res
