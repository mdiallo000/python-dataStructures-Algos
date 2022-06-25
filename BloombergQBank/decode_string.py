class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for i in range(len(s)):

            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ''

                while stack[-1] != "[":
                    substr = stack.popleft() + substr
