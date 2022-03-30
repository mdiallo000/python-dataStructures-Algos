# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, str: str) -> int:
        my_dict = {}
        for char in str:
            if char not in my_dict:
                my_dict[char] = 1
            else:
                my_dict[char] += 1

        for idx, elm in enumerate(str):
            if my_dict[elm] == 1:
                return idx

        return -1

    def With_a_set(sefl, str):
        myDict = {}
        seen = ()
        