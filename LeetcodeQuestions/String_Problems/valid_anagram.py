

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_collection = {}
        for char in s:
            my_collection[char] = 0

        for T in t:
            if T in my_collection:
                return True
        return False
