class Solution:
    def isValid(self, s: str):
        hash_map = {
            ")": "(",
            "]": '[',
            '}': '{'
        }
        stack = []

        for char in s
