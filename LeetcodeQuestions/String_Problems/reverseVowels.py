

class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 0: 
            return  
        vowels = {}
        left = 0
        right = len(s)-1

        while(left < right):
           if elem in s =='O' or '':
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            left += 1
            right -= 1
        return s
