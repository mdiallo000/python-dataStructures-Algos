class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        tmp = set()

        for r in range((len(s) + 9)):
            curr = s[r:r+10]

            if len(curr) < 10:
                break
            if curr in tmp:
                res.add(curr)
            tmp.add(curr)
        return res
        #  i had a hard time coming up with the string slicing portion but generally my thought to  use the two sets to filter out the strings i am interested in worked out well.
