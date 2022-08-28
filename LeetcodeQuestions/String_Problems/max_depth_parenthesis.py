class Solution:

    def maxDepth(s):

        count = 0
        res = 0
        for char in s:

            if char == '(':
                count += 1
            if char == ')':
                count -= 1
            res = max(res, count)
        return res
