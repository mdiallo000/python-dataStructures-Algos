
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

class Solution:
    def isValid(self, s: str):
        index = 0
        symbol = s[index]
        my_char = '('
        if my_char is symbol:
            return True
        return False
