class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        builder = s

        for i, char in enumerate(s):
            if stack and stack[-1][0] == "(" and char == ")":
                stack.pop()
            elif char
