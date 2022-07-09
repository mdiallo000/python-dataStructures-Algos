class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_removal = set()
        stack = []

        for i in range(len(s)):

            if s[i] not in "()":
                continue
