class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #  the parameters to generate parentheses is this:
        #  if at any point we have the same ammount of closed, open parenthese as required by n
        #  we cant keep adding open brakets if its surpassing n and we can add closed brakets if it will surpass the amount of closing brakets we have

        stack = []
        res = []

        def generate(openB, closedB):

            if openB == closedB == n:
                res.append(''.join(stack))
                return

            if openB < n:
                stack.append("(")
                generate(openB + 1, closedB)
                stack.pop()

            if closedB < openB:
                stack.append(")")
