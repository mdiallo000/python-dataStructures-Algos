class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        r, l, count = 0
        charMap = {}

        while r < len(s)-1:
            char = s[r]
            if char not in charMap:
                charMap[char] = 1
            else:
                charMap[char] += 1
