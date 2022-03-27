# A palimdrome is a word that can be writing both fowards and backwards. ex: Bob, racecar ect.

#  amanaplanacanalpanama
#  l                   r

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return all(s[1:] == s[:-1] for i in range(len(s)//2))
