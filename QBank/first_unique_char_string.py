class Solution:
    def firstUnique(self, str: word):
        char_dict = {}

        for char in word:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] = 2

        for idx, elm in enumerate(word):
            if char_dict[elm] == 1:
                return idx
        return -1
