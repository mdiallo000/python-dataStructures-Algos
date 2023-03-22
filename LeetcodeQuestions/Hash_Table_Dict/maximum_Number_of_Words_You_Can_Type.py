from collections import defaultdict


class Solution:

    def canBeTypedWord(self, text, brokenLetters):

        map_words = defaultdict(set)
        text = text.split(" ")

        for w in text:
            for c in w:
                map_words[w].add(c)
