class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        count = 0

        for char in s:
            if char == "(":
                count += 1
                if count > 1:
                    res += char
