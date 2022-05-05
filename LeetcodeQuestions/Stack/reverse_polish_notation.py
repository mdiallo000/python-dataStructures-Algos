class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '*'
            elif char == '-'
            elif char == '/'
            else:
                stack.append(int(char))
