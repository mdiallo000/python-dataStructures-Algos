class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0

        for i in range(len(s)):
            curr = values[s[i]]
            if i + 1 < len(s) and curr < values[s[i+1]]:
                res += -curr
            else:
                res += curr
        return res
#  the whole trick to this problem boils down to whether or not the curr character is greater or smaller than the one next to it,
#  if its greater than add it to the result, if its less than than subtract it to the result

#  Time complexity O(n)
#  Space complexity O(1)
