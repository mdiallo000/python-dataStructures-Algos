

from email import charset


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l, r = 0
        sub_string_count = 0
        # abcabc
        # l  r
        #   [a b c ]
        for r in range(len(s)):

            while s[r] in charSet:
                charset.remove(s[l])
                l += 1
            sub_string_count = max(sub_string_count, r-l + 1)
        return sub_string_count
