# A palimdrome is a word that can be writing both fowards and backwards. ex: Bob, racecar ect.

#  amanaplanacanalpanama
#  l                   r

from hashlib import new


class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowedWord = '0123456789qwertyuiopasdfghjklzxcvbnm'
        newStr = ''
        for char in s:
            if char not in allowedWord:
                continue
            else:
                newStr += char

        left = 0
        right = len(s)
        while left < right:
            if s[left] != s[right]:
                return False
