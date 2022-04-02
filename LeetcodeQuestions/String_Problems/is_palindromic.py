# A palimdrome is a word that can be writing both fowards and backwards. ex: Bob, racecar ect.

#  amanaplanacanalpanama
#  l                   r

from hashlib import new


class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowedWord = '0123456789qwertyuiopasdfghjklzxcvbnm'
        newStr = ''
        s = s.lower()
        for char in s:
            if char not in allowedWord:
                continue
            else:
                newStr += char

        left = 0
        right = len(newStr)-1
        while left < right:
            if newStr[left] != newStr[right]:
                return False
            left += 1
            right -= 1
        return True
