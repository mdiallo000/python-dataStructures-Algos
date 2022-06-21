class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "]":
                decoded = []
                while stack[-1] != "[":
                    decoded.append(stack.pop())

                stack.pop()
                base = 1
                k = 0
                while stack and stack[-1].isdigit():
                    k = k + (stack.pop()) * base
                    base *= 10
                while k != 0:
                    for i in range(len(decoded)-1, -1, -1):
                        stack.append(decoded[i])
                    k -= 1
            else:
                stack.append(char)
    #         result = [] * len(stack)
    #         for i in range(len(result)):
    #             result[i] = stack.pop()
        res = ""
        for char in stack:
            res += char
        return res
