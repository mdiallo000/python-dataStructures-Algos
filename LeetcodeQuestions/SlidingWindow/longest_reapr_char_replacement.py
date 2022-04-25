class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        count = 0
        charMap = {}
        # [A B B A B B A A]
        #      L         R
        maxf = 0
        for r in range(len(s)):
            char = s[r]
            if char not in charMap:
                charMap[char] = 1
            else:
                charMap[char] += 1
            window = r - l + 1

            maxf = max(maxf, charMap[s[r]])

            if window - maxf > k:
                charMap[s[l]] -= 1
                l += 1

            count = max(count, r - l + 1)
        return count
