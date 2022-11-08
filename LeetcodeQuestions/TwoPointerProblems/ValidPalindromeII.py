class Solution:
    def validPalindrome(self, s: str) -> bool:

        def palindrome(wrd, l, r):

            while l < r:
                if wrd[l] != wrd[r]:
                    return False
                l += 1
                r -= 1
            return True
