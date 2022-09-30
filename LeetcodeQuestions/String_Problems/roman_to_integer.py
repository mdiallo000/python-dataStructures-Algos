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
            print(curr)
            if i == len(s):
                res = curr
                break
            if curr > values[s[i+1]]:
                print(values[s[i+1]])
                res += curr
            else:
                res += -curr
        return res
