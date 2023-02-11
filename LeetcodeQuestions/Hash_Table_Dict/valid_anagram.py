# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # an anagram is defined as two words that have an equal amount of characters at the same frequency
        # So we can optimally solve this problem by getting a count of the two words and if they do then we have determined that these are anagrams of one another.
        #  simple pythonic solution:
        # return Counter(s) == Counter(t)

        #  More fleshed out solution:
        if len(s) != len(t):
            return False
        t_count = defaultdict(int)
        s_count = defaultdict(int)

        for s_char, t_char in zip(s, t):
            s_count[s_char] += 1
            t_count[t_char] += 1

        return s_count == t_count
    #  both solution use O(n) extra space to get a count of the characters. Time complexity is Linear O(n)
