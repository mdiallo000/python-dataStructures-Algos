class Solution:
    def minDeletions(self, s: str) -> int:
        count = [] * 26

        for char in s:
            count[ord('char') - ord('a')] += 1
