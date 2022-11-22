class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        oBrackets = 0
        cBrackets = 0

        for char in s:

            if stack and oBrackets < cBrackets:
                continue
            if char == "(":
