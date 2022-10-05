from calendar import c


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #  Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

        # You can use each character in text at most once. Return the maximum number of instances that can be formed.

        count = {}
        for char in text:
            if char in "balloon"
