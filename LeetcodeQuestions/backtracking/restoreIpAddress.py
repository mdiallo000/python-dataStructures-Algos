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
