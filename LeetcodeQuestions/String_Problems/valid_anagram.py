

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
        # my_set = ()
        # for char in s:
        #     my_set.add(char)

        # for T in t:
        #     if T in my_set:
        #         return True
        # return False
