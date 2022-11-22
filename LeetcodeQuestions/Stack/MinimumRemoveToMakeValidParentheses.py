class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        builder = s

        for i, val in enumerate(s):
