
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# To solve this problem we can use both a stack and a dictionary
# The dictionary will keep track of the brackets
class Solution:
    def isValid(self, s: str):
        # s= ex:'(){}[]' 
      
        stack = []
        closed_brackets = {
            ")" :"(",
            "]" : "[",
            "}" : "{"
        }
        
        for char in s:
         
         if char in closed_brackets:
            
            if stack and stack[-1] == closed_brackets[char]:
                stack.pop()
            
            else: return False
         
         else:
             stack.append(char)
    
        return True if stack == [] else False 
            
            