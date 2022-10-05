

from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #  Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

        # You can use each character in text at most once. Return the maximum number of instances that can be formed.

        count = defaultdict(int)
        for char in text:
            if char in "balloon":
                count[char] += 1
        res = 0
        while count:
            s = ""
            for char in "balloon":
                if char in count:
                    s += char
                    count[char] -= 1
                if count[char] == 0:
                    del count[char]
            if s == "balloon":
                res += 1
            if (sum(count.values())) < len('balloon'):
                break
        return res
