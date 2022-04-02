

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_collection = {}
        for char in s:
            my_collection[char] = 0

        for T in t:
            if T in my_collection:
                return True
            else:
                return False
        return False

    def is_Valid(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        for char in s:
            if T in t == char:
                return True
        return False

    def valid_anagram(self, s: str, t: str) -> bool:
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
