class Solution:
    def validPalindrome(self, s: str) -> bool:

        def palindrome(wrd, l, r):

            if wrd[l] != wrd[r]:
                return False
            return True
