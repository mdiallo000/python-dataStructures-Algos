# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # so we are getting two strings, needle and haystack
        #  the goal is to find where needle will occur inside of haystrack
        #  ie haystack = sadbustsad; needle = sad,
        # `    here we see that there are two occurences of sad in haystack but w
        #  we are only interested in return the first occurence of sad which is index 0 rather than 6

        #  one edge case we can handle right away is if needle is ever larger than haystack in that case we should just return -1
