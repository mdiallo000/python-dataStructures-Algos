class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s) + 1] = True

        for i in range(len(s)-1, -1, -1):
