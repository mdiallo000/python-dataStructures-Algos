class Solution:
    def validPalindrome(self, s: str) -> bool:

        def palindrome(wrd, l, r):

            while l < r:
                if wrd[l] != wrd[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:

            if s[l] != s[r]:
                return palindrome(s, l+1, r) or palindrome(s, l, r - 1)
            l += 1
            r -= 1
        return True
