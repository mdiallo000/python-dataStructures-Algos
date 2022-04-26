

from email import charset


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l = 0
        sub_string_count = 0
        # abceabecabc
        # l   r
        #   [        a b c]
        for r in range(len(s)):

            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            sub_string_count = max(sub_string_count, len(charSet))
        return sub_string_count
