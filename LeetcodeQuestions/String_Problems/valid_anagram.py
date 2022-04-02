

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
