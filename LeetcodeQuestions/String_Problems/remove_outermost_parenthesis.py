class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        count = 0

        for char in s:
            if char == "(":
                count += 1
                if count > 1:
                    res += char
            if char == ")":
                count -= 1
                if count > 0:
                    res += char

        return res
    #  Lessons learned
        #  we can solve the problem in linear time by keeping a count of the amount of closed and open brackets that we see, by doing so we can ignore the outer parentheses based on how balanced things are
