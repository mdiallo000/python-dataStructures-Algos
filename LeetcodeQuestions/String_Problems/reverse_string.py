# Write a function that reverses a string. The input string is given as an array of characters s.

# ex: Input: s = ["h","e","l","l","o"]
#  Output: ["o","l","l","e","h"]

from turtle import right


class Solution:
    def reverseString(self, s: List[str]):
        if len(s) == 0: 
            return  
       
        left = 0
        right = len(s)-1

        while(left < right):
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            left += 1
            right -= 1
        return s
