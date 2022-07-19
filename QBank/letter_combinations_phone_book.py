class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        charMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def generate(idx, currStr):

            if len(currStr) == len(digits):
                res.append(currStr)
                return

            for char in charMap[digits[idx]]:
                generate(idx+1, currStr + char)

        #  last chech makes sure we are not
        if digits:
            generate(0, '')
            return res
