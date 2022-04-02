

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1

        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1

        return True if s_dict == t_dict else False

# This solution has 0(1) space complexity since once we create our Hash MAP we arent inputing more characters. It will remain constant

# The Big O(n)
